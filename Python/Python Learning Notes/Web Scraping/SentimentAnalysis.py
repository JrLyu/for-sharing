# Import modules
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm import tqdm
import datetime
import numpy as np
from transformers import pipeline, DistilBertTokenizer, \
    DistilBertForSequenceClassification
import requests
from bs4 import BeautifulSoup
import pickle as pk


def get_trending_tickers():
    """
    Fetch the current trending tickers from Slickcharts.

    Returns:
    - list: List of ticker symbols.
    """
    url = 'https://www.slickcharts.com/sp500'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    tickers = [a.text for a in
               soup.select('.table-responsive table tbody tr td a')]
    return tickers


# Initialize the tokenizer and model
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertForSequenceClassification.from_pretrained(
    'distilbert-base-uncased-finetuned-sst-2-english')

# Create a sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model=model,
                              tokenizer=tokenizer)


def get_sentiment(text):
    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Truncate or split the tokens if they exceed the max length
    if len(tokens) > 512:
        tokens = tokens[:512]  # Truncate the tokens

    # Convert tokens to model inputs
    inputs = tokenizer.convert_tokens_to_ids(tokens)
    inputs = tokenizer.prepare_for_model(inputs, padding='max_length',
                                         max_length=512, truncation=True,
                                         return_tensors='pt')

    # Get model output
    output = model(**inputs)

    # Convert output to sentiment
    sentiment = 'POSITIVE' if np.argmax(
        output.logits).item() == 1 else 'NEGATIVE'

    return sentiment


def sentimentNLTK(data):
    """
    This function calculates the sentiment score for a given stock ticker.
        :param my_code: Stock ticker
        :return: Sentiment score
    """
    ticker, name, head, content = data

    analyzer = SentimentIntensityAnalyzer()
    # Create a data set containing the sentiment scores
    compound = []
    for j in range(len(content)):
        sentiment_dic = analyzer.polarity_scores(content[j, 1])
        compound.append(sentiment_dic["compound"])
    sentiment_score = pd.DataFrame({"Compound": compound})

    return np.mean(np.array(sentiment_score), axis=0)[0]


def sentimentBERT(data):
    """
    This function calculates the sentiment score for a given stock ticker using neural network.
        :param my_code: Stock ticker
        :return: Sentiment score
    """
    # Import the dataset

    ticker, name, head, content = data

    # Validate the DataFrame has the expected columns
    if len(content) < 1:  # Check if there are at least two columns
        raise ValueError(
            f"The CSV file for {ticker} does not have the expected number of columns.")

    content = np.array(content)[:, 0]

    # Calculate sentiment scores
    total = 0
    n = 0
    for c in content:
        n += 1
        sent = get_sentiment(c)
        if sent == "POSITIVE":
            total += 1
        elif sent == "NEGATIVE":
            total -= 1
    total /= n

    return total


def sentiment_analysis(method, data):
    """
    Get sentiment analysis scores for given codes using the specified method.
    :param method: 'BERT' or 'NLTK' - the method to use for sentiment analysis.
    :param codes: List of stock tickers.
    :return: DataFrame with sentiment scores.
    """
    codes = []
    for d in data:
        codes += [d[0]]

    sentiment_scores = []
    # (ticker, name, head, content)
    for info in data:
        sentiment_scores += [method(info)]

    valid_indices = [i for i, score in enumerate(sentiment_scores) if
                     score is not None]
    sentiment_scores = [sentiment_scores[i] for i in valid_indices]
    codes = [codes[i] for i in valid_indices]

    # Create a dataframe with the results
    sentiment_df = pd.DataFrame({
        "Ticker": codes,
        "Sentiment Score": sentiment_scores
    })

    # Sort the dataframe by sentiment score
    sentiment_df.sort_values("Sentiment Score", ascending=False, inplace=True)

    return sentiment_df


# Choose your method: 'BERT' or 'NLTK'
method = sentimentNLTK  # or 'NLTK'

fileName = "data.txt"
with open(fileName, 'rb') as f:
    data = pk.load(f)  # (ticker, name, head, content)xN
f.close()

sentiment_df = sentiment_analysis(method, data)

sentiment_df.to_csv(f"new_data/sentiment_{datetime.date.today()}_{method}.csv",
                    index=False)

print(
    f"Top 5 Stocks with Highest Sentiment Score using {method}: \n\n{sentiment_df.head(5)}")
print(
    f"5 Stocks with Lowest Sentiment Score using {method}:\n\n{sentiment_df.tail(5)}")
