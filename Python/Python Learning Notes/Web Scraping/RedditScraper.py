import praw
import pandas as pd
from tqdm import tqdm

reddit = praw.Reddit(client_id="USJLd7IZqY0yWOAFWa_XGw",
                     client_secret="XV1JnXrCKQpyNuc34sQEyDaKBO4z8g",
                     user_agent="AlgoryCapitalScraper by u/i-illuminati")


def get_posts(sub, n):
    """
    This function scrapes the posts from a given subreddit.
    Param
        :sub: subreddit name
        :n: number of posts
    """

    subreddit = reddit.subreddit(sub)
    posts = []
    for post in tqdm(subreddit.hot(limit=n)):
        posts.append(
            [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

    posts.to_pickle("./posts.pkl")


def get_comments(file):
    """
    This function scrapes the comments from a given subreddit.
    Param
        :file: file path
    """
    posts = pd.read_pickle(file)
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

    comments.to_pickle("./comments.pkl")


def match_tickers(file, tickers):
    df = pd.read_pickle(file)
    # Incomplete...



get_posts("wallstreetbets", 20)
get_comments("./posts.pkl")