from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url='https://en.wikipedia.org/wiki/List_of_parks_in_Singapore'
page = requests.get(url)

soup = BeautifulSoup(page.text , 'html.parser')

table = soup.find_all('table' ,{"class":"wikitable sortable"})
table = table[0]

table_titles = table.find_all('th')
park_table_titles = [title.text for title in table_titles]
df = pd.DataFrame(columns=park_table_titles)
df = df.rename(columns={'Name':'Name' , 'Type':'Types', 'Area (m\n\n\n\n\n\n\n2\n\n\n\n\n{\\displaystyle ^{2}}\n\n)\n':'Area'})

column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data
df.drop('Area', axis='columns', inplace=True)

def get_park_list():
    all_park_names = list(df['Name'])
    return all_park_names

def get_park_coordinates():
    park_coord = pd.read_csv('Data/Coordinates/park_coordinates.csv')
    park_coord = park_coord[['address','LATITUDE','LONGITUDE']]
    park_coord = park_coord.drop_duplicates(subset=['address'])
    park_coord = park_coord.reset_index(drop=True)
    return park_coord

