import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import GetData

# Get the dataframe
sentiment_df = pd.read_csv("new_data/sentiment_2023-10-20.csv")
stocks = GetData.get_code()

# distribution of sentiment score
sns.histplot(sentiment_df["Sentiment Score"], kde = True)
plt.title('Distribution of Sentiment Scores')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

print(f"Top 20 Stocks with Highest Sentiment Score: \n\n{sentiment_df.head(20)}")
