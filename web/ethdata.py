from bs4 import BeautifulSoup
import requests
import re

eth_usd_url = 'https://www.coingecko.com/en/price_charts/ethereum/usd'


def get_eth_usd():
    response = requests.get(eth_usd_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')

    eth_line_regex = re.compile('^.*Ethereum price for today is.*$', re.DOTALL)
    eth_value_regex = re.compile('[0-9]+\.[0-9]+')
    for paragraph in paragraphs:
        paragraph_lines = paragraph.text.split('\n')
        for paragraph_line in paragraph_lines:
            if eth_line_regex.match(paragraph_line):
                print(eth_value_regex.search(paragraph_line).group(0))


get_eth_usd()
