
#Import the diferent libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests

source = requests.get('https://slickdeals.net/laptop-deals/').text

soup = BeautifulSoup(source, 'lxml')

Descriptions=[]
Ratings=[]
Prices=[]


for data in soup.find_all('div', class_='fpItem'):
    description = data.find('a', class_='itemTitle bp-c-link')
    Descriptions.append(description.text)

    price = data.find('div', class_='priceLine')
    Prices.append(price.text.split()[0])

    rating = data.find('span', class_='count')
    Ratings.append(rating.text)

df = pd.DataFrame({'Description':Descriptions, 'Price':Prices, 'Rating':Ratings})
df.to_csv('EcomerceScraping.csv')
