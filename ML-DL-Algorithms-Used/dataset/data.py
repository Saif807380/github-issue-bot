import requests
import pandas as pd
import json
from dotenv import load_dotenv
import os
import sys

load_dotenv()

if os.path.exists("dataset.csv"):
    df = pd.read_csv("dataset.csv")
    df.drop(["Unnamed: 0"], axis=1, inplace=True)
else:
    df = pd.DataFrame({
        "url": [],
        "repo": [],
        "title": [],
        "body": [],
        "labels": []
    })

print(df.shape)

language = sys.argv[1]
label = sys.argv[2]

# labels: bug, documentation, docs, enhancement, feature, question, design, improvement, help
for page in range(1, 11):
    print("Current page:", page)
    response = requests.get(
        "https://api.github.com/search/issues",
        params = { "q": f"language:{language} label:{label}", "per_page": 100, "page": page },
        headers =  { "Accept": "application/vnd.github.v3+json" },
        auth = (os.getenv('GITHUB_USERNAME'), os.getenv('PERSONAL_ACCESS_TOKEN'))
    )
    if response.status_code == 200:
        json_response = response.json()
        df2 = {
            "url": [],
            "repo": [],
            "title": [],
            "body": [],
            "labels": [],
        }
        for item in json_response["items"]:
            df2["url"].append(item["html_url"])
            df2["repo"].append(item["repository_url"].split("/")[-2] + "/" + item["repository_url"].split("/")[-1])
            df2["title"].append(item["title"])
            df2["body"].append(item["body"])
            df2["labels"].append(label)
        df = pd.concat([df, pd.DataFrame(df2)], ignore_index=True).drop_duplicates().reset_index(drop=True)
    else:
        print(response.content)

print(df.shape)
df.to_csv("dataset.csv")
