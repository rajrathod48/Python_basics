import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
#import features


base_url = "https://www.espncricinfo.com/"
url = "https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/match-schedule-fixtures-and-results"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup)

div_tags = soup.find_all('div', {'class' : 'ds-p-0'})


links = []
for div in div_tags:
    a_tags = div.find_all('a')
    for a in a_tags:
        # print(a)
        if a['href'].endswith('full-scorecard'):
            links.append(base_url + a['href'])
            # print(links)

df_links = pd.DataFrame({'Links' :links})

mvplinks = df_links.to_csv(index = False)

# print(mvplinks)

with open ('mvplinks.csv', 'w') as f:
    f.write(mvplinks)

# print(df_links.head())

for link in links:
    new_url = link.replace('/full-scorecard', '/match-impact-player')

    response = requests.get(new_url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    table_tag = soup.find('table', class_ = 'ds-w-full ds-table ds-table-md ds-table-auto')

    #convert table data to a pandas df
    df = pd.read_html(str(table_tag))[0]

    #top 11 most valuable player
    print(df.head(11))
    top11 = df.head(11)

    if os.path.isfile('mvpdata.csv') and os.path.getsize('mvpdata.csv') >0:
        with open('mvpdata.csv', 'a') as f:
            csv_data = top11.to_csv(header = False, index = False)
            f.write(csv_data)
    
    else:
        with open('mvpdata.csv', 'a') as f:
            csv_data = top11.to_csv(header = True, index = False)
            f.write(csv_data)
            
mvpdata = pd.read_csv("mvpdata.csv")

print(mvpdata.describe())

