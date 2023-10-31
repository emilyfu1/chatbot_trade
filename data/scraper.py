import os
import pandas as pd
import time
import requests
from requests import get
from bs4 import BeautifulSoup
import os.path as path

hs616285 = ['61', '62', '85']

def hs6dataset(hs2codes):    
# empty dataframe
    hs6codes = pd.DataFrame(columns=['hs4', 'hs6', 'desc'])

    # go through specified HS2 codes
    for code in hs2codes:
        url = 'https://www.foreign-trade.com/reference/hscode.htm?code=' + code
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'}

        response = requests.get(url, headers=headers)
        # converts HTML to python-readable
        soup = BeautifulSoup(response.content, "html.parser")
        # finds <td> HTML elements (these store the HS codes and their descriptions)
        products = soup.find_all('td')
        # loop through HS4 codes to find HS6 codes
        for product in products:
            if product.find('a'):
                hs4 = product.text
                # URL where table of HS6 codes is located
                urlhs6 = 'https://www.foreign-trade.com/reference/hscode.htm?code=' + hs4
                responsehs6 = requests.get(urlhs6, headers=headers)
                # converts HTML to python-readable
                souphs6 = BeautifulSoup(responsehs6.content, "html.parser")

                # finds <tr> HTML elements where the HS6 codes are stored
                productshs6 = souphs6.find_all('tr')
                for producths6 in productshs6:
                    hs6 = producths6.find('b').text
                    desc = producths6.find_all('td')[1].text
                    row = [hs4, hs6, desc]
                    hs6codes.loc[len(hs6codes)] = row
    
    return hs6codes

data = hs6dataset(hs616285)
data.to_csv('data/hs6codes.csv')

