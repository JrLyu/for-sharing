# Import modules
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from tqdm import tqdm
import GetData
import datetime

def sentiment(my_code):
    """
    This function calculates the sentiment score for a given stock ticker.
        :param my_code: Stock ticker
        :return: Sentiment score
    """
    # Import the dataset
    df = pd.read_csv(f"data/{my_code}.csv")
    analyzer = SentimentIntensityAnalyzer()
    # Create a data set containing the sentiment scores
    compound = []
    for j in range(len(df)):
        sentiment_dic = analyzer.polarity_scores(df.iloc[j, 1])
        compound.append(sentiment_dic["compound"])
    sentiment_score = pd.DataFrame({"Compound": compound})

    return float(sentiment_score.mean())


code = GetData.get_code()
ticker = []
sentimentScore = []
for i in tqdm(range(len(code))):
    sentimentScore.append(sentiment(code[i]))
    ticker.append(code[i])

sentiment_df = pd.DataFrame({"Ticker": ticker, "Sentiment Score": sentimentScore})
sentiment_df.sort_values("Sentiment Score", ascending=False, inplace=True)
sentiment_df.to_csv(f"new_data/sentiment_{datetime.date.today()}.csv", index=False)

# sentiment_df.dropna()

print(f"Top 50 Stocks with Highest Sentiment Score: \n\n{sentiment_df.head(50)}")

print(f"50 Stocks with Lowest Sentiment Score:\n\n{sentiment_df.dropna().tail(50)}")
