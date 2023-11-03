import re
import praw
import pandas as pd
import numpy as np
from tqdm import tqdm
import GetData

reddit = praw.Reddit(client_id="USJLd7IZqY0yWOAFWa_XGw",
                     client_secret="XV1JnXrCKQpyNuc34sQEyDaKBO4z8g",
                     user_agent="AlgoryCapitalScraper by u/i-illuminati")

def get_posts(sub, n=100):
    """
    This function scrapes the posts from a given subreddit.
    Param
        :sub: subreddit name
        :n: number of posts
    """

    subreddit = reddit.subreddit(sub)
    posts = []
    for post in tqdm(subreddit.top(time_filter="all", limit=n)):
        posts.append(
            [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

    posts.to_csv("./posts.csv")


def get_comments(file):
    """
    This function scrapes the comments from a given subreddit.
    Param
        :file: file path
    """
    posts = pd.read_csv(file)
    comments = []
    for url in tqdm(posts['url']):
        try:
            submission = reddit.submission(url=url)
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                comments.append(comment.body)
        except:
            continue
    comments = pd.DataFrame(comments, columns=['body'])

    comments.to_csv("./comments.csv")


def match_tickers(file, tickers):
    """
    This function matches the stock tickers in the comments.
    It will save the matched comments to a responding pickle file.
    Param
        :file: file path
        :tickers: stock tickers
    """
    df = pd.read_csv(file)
    for ticker in tqdm(tickers):
        body_ticker = []
        body_ticker_not_found = []
        for i in range(len(df)):
            comment = df.iloc[i, 1]
            if isinstance(comment, str):
                ticker_matches = re.findall(rf"\b{re.escape(ticker)}\b", comment)  # Using regex for word boundary check
                if ticker_matches:
                    body_ticker.append(comment)
        if body_ticker:  # Proceed if the list is not empty for a particular ticker
            body_ticker_df = pd.DataFrame(body_ticker, columns=['body'])
            body_ticker_df.to_csv(f"data/{ticker}.csv")  # Save the DataFrame to CSV
        else:
            body_ticker_not_found.append(ticker)
    print("Done!")
    if body_ticker_not_found:
        print(f"Tickers not found in comments:")
        for ticker in body_ticker_not_found:
            print(ticker)



get_posts("finance+wallstreetbets+cryptocurrency+investing+InvestmentClub+Stockmarkets+Stock_Picks\
          +options+personalfinance", n=1000)
get_comments("./posts.csv")
match_tickers("./comments.csv", GetData.get_code())