from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


url='https://en.wikipedia.org/wiki/List_of_shopping_malls_in_Singapore'
page = requests.get(url)
soup = BeautifulSoup(page.text , 'html.parser')
malls = soup.find_all('div' ,{"class":"div-col"})
def get_mall_list():
    mall_lst =[]
    for div in malls:
        for li in div.find_all('li'):
            print(li.get_text())
            mall_lst.append(li.get_text())
    return mall_lst

def get_mall_coordinates():
    mall_coord = pd.read_csv('Data/Coordinates/mall_coordinates.csv')
    mall_coord = mall_coord[['address','LATITUDE','LONGITUDE']]
    mall_coord = mall_coord.drop_duplicates(subset=['address'])
    mall_coord = mall_coord.reset_index(drop=True)
    mall_coord['address'] = mall_coord['address'].str.split('[').str[0]
    return mall_coord.head(27)


print(get_mall_coordinates())