from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url = 'https://schoolbell.sg/primary-school-ranking/'

page = requests.get(url)

soup = BeautifulSoup(page.text , 'html.parser')
table = soup.find_all('table')[1]

table_titles = table.find_all('th')
school_table_titles = [title.text for title in table_titles]

df = pd.DataFrame(columns=school_table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text for data in row_data]
    if len(individual_row_data) < 3:
       if previous_row_data is not None:
           individual_row_data = [previous_row_data[0]] + individual_row_data + [previous_row_data[2]]
       
    if len(individual_row_data) >= 3:
        length = len(df)
        df.loc[length] = individual_row_data

    previous_row_data = individual_row_data

#get the top 50 schools in sg
df.index = np.arange(1, len(df) + 1)
df=df.iloc[:50]

#function to return list of school names
def get_school_list():
    all_school_names = list(df['Primary School'])
    return all_school_names

def get_school_coordinates():
    #filter to address , X , Y and remove duplicates
    school_coord = pd.read_csv('Data/Coordinates/School_coordinates.csv')
    school_coord = school_coord[['address','LATITUDE','LONGITUDE']]
    school_coord = school_coord.drop_duplicates(subset=['address'])
    school_coord = school_coord.reset_index(drop=True)
    return school_coord