from bs4 import BeautifulSoup
import requests
import pandas as pd

import sys
reload(sys)
sys.setdefaultencoding('utf8')

source = requests.get('https://en.wikipedia.org/wiki/List_of_largest_manufacturing_companies_by_revenue').text

soup = BeautifulSoup(source, 'html5lib')

#print(soup.prettify().encode("utf-8"))

table = soup.find('table', {'class': 'wikitable sortable plainrowheads'})
#print(table)
rows = table.find_all('tr')

columns = [v.text.replace('\n',' ') for v in rows[0].find_all('th')]

#print(columns)

df = pd.DataFrame(columns=columns)

for i in range(1,len(rows)):
    tds = rows[i].find_all('td')

    if isinstance(tds[0].text.replace('\n',''), str):
        tds[0].text = unicode(tds[0].text.replace('\n',''), "utf-8")
    if isinstance(tds[1].text.replace('\n',''), str):
        tds[1].text = unicode(tds[1].text.replace('\n',''), "utf-8")
    if isinstance(tds[2].text.replace('\n',''), str):
        tds[2].text = unicode(tds[2].text.replace('\n',''), "utf-8")
    if isinstance(tds[3].text.replace('\n',''), str):
        tds[3].text = unicode(tds[3].text.replace('\n',''), "utf-8")
    if isinstance(tds[4].text.replace('\n',''), str):
        tds[4].text = unicode(tds[4].text.replace('\n',''), "utf-8")

    values = [tds[0].text.replace('\n',''),tds[1].text.replace('\n',''),tds[2].text.replace('\n',''),tds[3].text.replace('\n',''),tds[4].text.replace('\n','')]

    #print(values)

    #break
    #values.encode('utf-8')

    df = df.append(pd.Series(values, index=columns), ignore_index = True)

    df.to_csv(r'C:\Users\rana.hardik\Desktop\Scrapping' + '\\table.csv', index=False)
