# Import modules
import pandas as pd
import datetime
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
import pickle as pk


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
        sentiment_dic = analyzer.polarity_scores(content[j])
        compound.append(sentiment_dic["compound"])
    sentiment_score = pd.DataFrame({"Compound": compound})

    return np.mean(np.array(sentiment_score), axis=0)[0]


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


method = sentimentNLTK  # or 'NLTK'

fileName = "dataYahoo.txt"
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
