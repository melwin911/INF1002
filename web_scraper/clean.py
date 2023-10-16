import pandas as pd
import hdb_scraper

df1 = pd.read_csv('web_scraper/Data/2012_merged.csv')
df2 = pd.read_csv('web_scraper/Data/Flat_amenities/final_amenities_merged.csv')

#inserting price and town column
town_column = df1.pop('town')
price_column = df1.pop('resale_price')
postal_column = hdb_scraper.get_hdb_postal()
df2.insert(0,'town',town_column)
df2.insert(2,'postal',postal_column)
df2['resale_price'] = price_column
df2 = df2.sort_values(by='town')

df2.to_csv('web_scraper/Data/final_sorted.csv',index=False)

