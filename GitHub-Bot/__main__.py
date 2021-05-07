import os
import aiohttp
from aiohttp import web
from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp
routes = web.RouteTableDef()
router = routing.Router()
import requests
import numpy as np
import pandas as pd
import torch
from torchtext.data.utils import get_tokenizer
from collections import Counter
from torchtext.vocab import Vocab
from torch import nn
import re
from bs4 import BeautifulSoup
from markdown import markdown
#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import nltk
nltk.download('punkt')
#stop_words = set(stopwords.words('english'))

from datanltk import palak
stop_words=palak
print(stop_words)
def de_emojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


def markdown_to_text(markdown_string):
    """ Converts a markdown string to plaintext """

    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown(markdown_string)

    # remove code snippets
    html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
    html = re.sub(r'<code>(.*?)</code >', ' ', html)

    # extract text
    soup = BeautifulSoup(html, "html.parser")
    text = ''.join(soup.findAll(text=True))

    return text

def clean(text):
    text = text.lower()
    text = re.sub(r"http\S+", " ", text)
    text = text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
    text = text.translate(str.maketrans(string.digits, ' '*len(string.digits)))
    tokens = word_tokenize(text)
    text = " ".join([token for token in tokens if token not in stop_words])
    return text



class TextClassificationModel(nn.Module):
  def __init__(self, vocab_size, embed_dim, num_class):
    super(TextClassificationModel, self).__init__()
    self.embedding = nn.EmbeddingBag(vocab_size, embed_dim, sparse=True)
    self.fc = nn.Linear(embed_dim, num_class)
    self.init_weights()

  def init_weights(self):
    initrange = 0.5
    self.embedding.weight.data.uniform_(-initrange, initrange)
    self.fc.weight.data.uniform_(-initrange, initrange)
    self.fc.bias.data.zero_()

  def forward(self, text, offsets):
    embedded = self.embedding(text, offsets)
    return self.fc(embedded)

df = pd.read_csv("processed.csv")

tokenizer = get_tokenizer('basic_english')
counter = Counter()
for idx, data in df.iterrows():
  counter.update(tokenizer(data["issue"]))
vocab = Vocab(counter, min_freq=1)

text_pipeline = lambda x: [vocab[token] for token in tokenizer(x)]

classes = {}
for i in range(6):
  classes[i] = df["label_name"][df["label"]==i].unique()[0]

model = torch.load("model.pth")
model.eval()

def predict(text):
    with torch.no_grad():
        text = torch.tensor(text_pipeline(text))
        output = model(text, torch.tensor([0]))
        return classes[output.argmax(1).item()]


@router.register("issues", action="opened")
async def issue_opened_event(event, gh, *args, **kwargs):
    """
    Whenever an issue is opened, greet the author and say thanks.
    """
    label_url = event.data["issue"]["labels_url"]
    comments_url = event.data["issue"]["comments_url"]
    author = event.data["issue"]["user"]["login"]
    print(event.data)
    print(event.data["issue"]["title"])
    print(event.data["issue"]["body"])
    text=event.data["issue"]["title"]+event.data["issue"]["body"]
    text=de_emojify(text)
    text=markdown_to_text(text)
    text=clean(text)
    print(text)
    issue_no=str(event.data["issue"]["number"])
    assigned_label = predict(text)
    message = f"Thanks for the report @{author}! I figured out that the following assigned issue belongs to a particular label i.e {assigned_label}! (I'm a bot)."
    #await gh.post(label_url, data={"": assigned_label})
    await gh.post(comments_url, data={"body": message})
    response = requests.post(
                event.data["issue"]["url"]+"/labels",
                headers =  { "Accept": "application/vnd.github.v3+json" },
                auth = ('label-decoder-bot', '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'),
                json={"labels":[assigned_label]}
    )

    

@routes.get("/", name="home")
async def handle_get(request):
    print("In / route")
    return web.Response(text="Hello world")

@routes.post("/")
async def main(request):
    body = await request.read()

    secret = "issue-label-ml-bot"
    #oauth_token = "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"
    oauth_token ="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"
    event = sansio.Event.from_http(request.headers, body, secret=secret)
    async with aiohttp.ClientSession() as session:
        gh = gh_aiohttp.GitHubAPI(session, "issue-label-ml-bot",
                                  oauth_token=oauth_token)
        await router.dispatch(event, gh)
    return web.Response(status=200)

if __name__ == "__main__":
    app = web.Application()
    app.router.add_routes(routes)
    port = os.environ.get("PORT")
    print(port)
    if port is not None:
        port = int(port)
    web.run_app(app, port=port or 8000)