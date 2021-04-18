# github-issue-bot

## Setup for running the notebooks

1. Clone the repo
```bash
  $ git clone https://github.com/Saif807380/github-issue-bot.git
```

2. Create a virtual environment and install the dependencies
```bash
  $ pip install -r requirements.txt
```

3. Download a `textblob` dependencies
```bash
  $ python -m textblob.download_corpora
```

4. Download `nltk` corpora by running this in the python interpreter
```bash
  $ python
```
```python
  import nltk
  nltk.download('stopwords')
  nltk.download('punkt')
```

## Setup for Building Dataset

Data is present inside the dataset folder. `data.sh` script executes `data.py`
and provides language and label name to generate the dataset.

### Languages

- Python
- JavaScript
- Java

### Labels

- bug
- documentation
- docs
- enhancement
- feature
- question
- design
- improvement
- help

1. Clone the repo
```bash
  $ git clone https://github.com/Saif807380/github-issue-bot.git
```

2. Create a virtual environment and install the dependencies
```bash
  $ pip install -r requirements.txt
```

3. Setup the `.env` file using the `.env.example` file

## Generating dataset

1. Make sure the `.env` file is setup correctly

2. Make `data.sh` executable
```bash
  $ chmod u+x dataset/data.sh
```

3. Execute the script
```bash
  $ dataset/data.sh
```
