import pandas as pd
import pickle as pk
import re
import praw
from tqdm import tqdm
import GetData

reddit = praw.Reddit(client_id="USJLd7IZqY0yWOAFWa_XGw",
                     client_secret="XV1JnXrCKQpyNuc34sQEyDaKBO4z8g",
                     user_agent="AlgoryCapitalScraper by u/i-illuminati")


def get_posts(subs, n=100, time_filter="week"):
    """
    This function scrapes the posts from a given subreddit.
    Param
        :sub: subreddit name
        :n: number of posts
            default: 100, maximum = 375
        :time_filter: time filter for subreddit posts
                      select from "all", "day", "hour", "month", "week", "year"
                      default: "week"
    """
    posts = []
    for sub in subs:
        subreddit = reddit.subreddit(sub)
        for post in tqdm(subreddit.hot(limit=n)):
            posts.append(
                [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created]
            )
    posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

    posts.to_csv("./posts.csv", index=False)
    print("Done!\n\n Distribution of the Subreddits:")
    print(posts["subreddit"].value_counts())


def get_comments(file, n=100):
    """
    This function scrapes the comments from a given subreddit.
    Param
        :file: file path
        :n: number of comments.
            default: 100
    """
    posts = pd.read_pickle(file)
    comments_dict = {'body': [], 'postNum': []}
    post_num = 0

    for url in tqdm(posts['url']):
        try:
            submission = reddit.submission(url=url)
            submission.comment_limit = n
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                comments_dict['body'].append(comment.body)
                comments_dict['postNum'].append(post_num)
            post_num += 1
        except:
            continue

    comments_df = pd.DataFrame(comments_dict)
    comments_df.to_csv("./comments.csv", index=False)
    comments_df.to_pickle("./comments.pkl")
    print("Done!")


def match_tickers(post_file, comment_file, tickers):
    """
    This function matches the stock tickers in the comments.
    It will save the matched comments to a responding pickle file.
    Param
        :file: file path
        :tickers: stock tickers
    """
    post_df = pd.read_pickle(post_file)
    comment_df = pd.read_pickle(comment_file)
    body_ticker_not_found = []
    data = []

    for ticker in tqdm(tickers):
        body_ticker = []

        # Check the post titles
        for i in range(len(post_df)):
            body = post_df.iloc[i, 6]
            if isinstance(body, str):
                ticker_matches = re.findall(rf"\b{re.escape(ticker)}\b", body)
                if ticker_matches:
                    body_ticker.append(body)

        # Check the comments
        for i in range(len(comment_df)):
            comment = comment_df.iloc[i, 0]
            if isinstance(comment, str):
                ticker_matches = re.findall(rf"\b{re.escape(ticker)}\b", comment)  # Using regex for word boundary check
                if ticker_matches:
                    body_ticker.append(comment)
                    continue  # Skip checking the post if the ticker is found in the comment

            # Check the corresponding post for the comment
            post_index = comment_df.iloc[i, 1]
            if isinstance(post_index, int) and 0 <= post_index < len(post_df):
                post = post_df.iloc[post_index, 6]
                if isinstance(post, str):
                    ticker_matches = re.findall(rf"\b{re.escape(ticker)}\b", post)
                    if ticker_matches:
                        body_ticker.append(comment)

        if body_ticker:  # Proceed if the list is not empty for a particular ticker
            data += [(ticker, body_ticker)]

            fileName = "data.txt"
            with open(fileName, 'wb') as f:
                pk.dump(data, f)
            f.close()
        else:
            body_ticker_not_found.append(ticker)

    print("Done!")
    print(f"Tickers not found in comments:")
    if body_ticker_not_found:
        for ticker in body_ticker_not_found:
            print(ticker)
    else:
        print("All tickers found in comments.")


# subs = ["wallstreetbets", "cryptocurrency", "investing", "stocks",
#         "personalfinance", "options", "robinhood", "stockmarket",
#         "investing_discussion", "investments"]
#
# get_posts(subs, n=5, time_filter="week")  # Get the posts
#
# get_comments("./posts.pkl", 5)  # Get the comments

match_tickers("./posts.pkl", "./comments.pkl", GetData.get_code())  # Match the tickers

fileName = "data.txt"
with open(fileName, 'rb') as f:
    data = pk.load(f)  # (ticker, name, head, content)xN
f.close()
print(data)