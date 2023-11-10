from bs4 import BeautifulSoup
import requests
import pandas as pd
from lxml import etree


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find_all('table')[1]
titles = table.find_all('th')
table_headers = [title.text.strip() for title in titles]
print(table_headers)
df = pd.DataFrame(columns = table_headers)

column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    separate_row_data = [data.text.strip() for data in row_data]

    lenght = len(df)
    df.loc[lenght] = separate_row_data
print(df)
df.to_csv(r'List_of_largest_companies_US.csv', sep='\t', index=False)
