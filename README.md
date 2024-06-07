# digikala-sentiment-analysis
Aspect based sentiment analysis on digikala products comment.

### Methods:
  1. Py-ABSA: Multilingual
  2. Using LLM for the whole thing.(Llama,phi-3)
  3. First Translate then English ABSA. (can use LLM for translation).


## Installation
```sh
git clone <url>
cd <project>
pip install virtualenv # (if you don't already have virtualenv installed)
virtualenv venv # to create your new environment (called 'venv' here)
source venv/bin/activate # to enter the virtual environment
pip install -r requirements.txt # to install the requirements in the current environment
```



## Refrences: 

[Github: Aspect-term extraction and Aspect-based sentiment analysis](https://github.com/nicolezattarin/BERT-Aspect-Based-Sentiment-Analysis)\
[ABSA datasets for PyABSA](https://github.com/yangheng95/ABSADatasets)\
[Aspect-based Sentiment Analysis](https://github.com/1tangerine1day/Aspect-Term-Extraction-and-Analysis)\
[Quick intro to Aspect-Based Sentiment Analysis](https://medium.com/nlplanet/quick-intro-to-aspect-based-sentiment-analysis-c8888a09eda7)\
[ParsBERT (v3.0)](https://huggingface.co/HooshvareLab/bert-fa-zwnj-base)