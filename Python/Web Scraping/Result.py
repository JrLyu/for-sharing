import pandas as pd
import numpy as np

# Read the csv file
df = pd.read_csv('new_data/totalSentiment.csv')
# df.columns = ["Ticker", "Yahoo Score", "Reddit Score", "Total(Average) Score"]
# df.drop(columns=["Ticker2"], inplace=True)

print(
    f"Top 5 Stocks with Highest Sentiment Score: \n{df.head(5)}\n")
print(
    f"5 Stocks with Lowest Sentiment Score:\n{df.tail(5)}\n")