from bs4 import BeautifulSoup
import requests
import re


__ETH_BASE_URL = 'https://www.coingecko.com/en/price_charts/ethereum/'

_eth_line_regex = re.compile('^.*Ethereum price for today is.*$', re.DOTALL)
_eth_price_regex = re.compile('[0-9]+\.[0-9]+')


# Returns latest price of ETH in USD
def get_eth_usd():
    return _get_eth_price('usd')

# Returns latest price of ETH in GBP
def get_eth_gbp():
    return _get_eth_price('gbp')


def _get_eth_price(currency):
    # Get HTML page specified by ETH_BASE_URL
    response = requests.get(__ETH_BASE_URL + currency)
    # Parse the HTML page to obtain the ETH price data
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        paragraph_lines = paragraph.text.split('\n')
        for paragraph_line in paragraph_lines:
            if _eth_line_regex.match(paragraph_line):
                return _eth_price_regex.search(paragraph_line).group(0)


print(get_eth_usd())
print(get_eth_gbp())
