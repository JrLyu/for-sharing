# import modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import SP500


# utility function to download a webpage and return a beautiful soup doc
def get_page(url):
    response = requests.get(url)
    page_content = response.text
    doc = BeautifulSoup(page_content, 'html.parser')
    return doc


# get the URL using response variable
def getData(code):
    """
    This function scrapes the news headlines from Yahoo Finance for a given stock ticker.
        :param code: Stock ticker
        :return: A csv file containing the news headlines
    """
    my_url = f"https://finance.yahoo.com/quote/{code}?p={code}"
    doc = get_page(my_url)
    # Appropriate tags common to news-headlines to filter out the necessary information.
    a_tags = doc.find_all('a', {'class': "js-content-viewer"})
    news_list = []
    for i in range(1, len(a_tags) + 1):
        news = a_tags[i - 1].text
        news_list.append(news)

    # Save news headlines to a csv file for sentiment analysis
    news_df = pd.DataFrame(news_list)
    news_df.to_csv(f"data/{code}.csv")


code = SP500.get_code()

for i in tqdm(range(len(code))):
    getData(code[i])
