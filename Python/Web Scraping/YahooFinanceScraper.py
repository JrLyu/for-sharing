import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import pickle as pk
import GetData

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

    tickers = [a.text for a in soup.select('.table-responsive table tbody tr td a')]
    return tickers

def get_page(url):
    """Utility function to download a webpage and return a beautiful soup doc."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching page {url}: {e}")
        return None

def get_news_data(code):
    """
    This function scrapes the news headlines and article bodies from Yahoo Finance
    for a given stock ticker and returns them as dataframes.
    """
    base_url = f"https://finance.yahoo.com/quote/{code}?p={code}"
    soup = get_page(base_url)
    if not soup:
        return None, None

    # Get headlines
    headlines = [item.text for item in soup.find_all('a', {'class': "js-content-viewer"})]

    # Get news article contents
    news_links = [item.a['href'] for item in soup.find_all('h3', class_='Mb(5px)')
                  if item.a and item.a['href'].startswith('/')]
    contents = []
    for link in news_links:
        full_url = "https://finance.yahoo.com" + link
        news_page = get_page(full_url)
        if news_page:
            paragraphs = news_page.find_all('p')
            article_content = ' '.join([para.get_text() for para in paragraphs])
            contents.append(article_content)
        else:
            contents += [""]

    return headlines, contents

all_sp500_stocks = get_trending_tickers()

# all_sp500_stocks = all_sp500_stocks[:10]

codes = all_sp500_stocks[1::2]
names = all_sp500_stocks[0::2]

data = []

for stock_code in tqdm(codes):
    data += [(stock_code, names.pop(0), *get_news_data(stock_code))] #ticker, name, head, content

fileName = "dataYahoo.txt"
with open(fileName, 'wb') as f:
    pk.dump(data, f)
f.close()
