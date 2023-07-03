import requests
from bs4 import BeautifulSoup
import urllib
import pandas as pd


def get_soup(url):
    user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    while True:
      link = requests.get(url, headers={'User-Agent': user})
      if link.status_code == 200:
        soup = BeautifulSoup(link.content, 'html.parser')
        break
    return soup


url = 'https://www.amazon.in/s?k=laptop&crid=2J7LCMD2BA4RR&sprefix=laptop%2Caps%2C298&ref=nb_sb_noss_1'
c = 0
v = 1
links = set()
df = pd.DataFrame()
while True:
    try:
      soup = get_soup(url)
      next_link = soup.find('a', {'class': 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator'}).get('href')
      links.add(url)
      print(url)
      if next_link is not None:
        url = 'https://amazon.in'+next_link

        c+=1
        print('Link : ', c)
        se = set()
        xyz = soup.find_all('h2', {'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'})
        for j in xyz:
          abc = j.find('a', {'class': "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}).get('href')
          se.add('https://amazon.in'+abc)
        se = list(se)
        print(len(se))
        z = 0
        while True:
            s = get_soup(se[z])
            try:
                a = []
                b = []
                data = s.find('table', {'class': 'a-normal a-spacing-micro'})
                #print(data.text)
                for i, y in zip(data.find_all('td', {'class': 'a-span3'}), data.find_all('td', {'class': 'a-span9'})):
                    a.append(i.text)
                    b.append(y.text)
                a.append('Price')
                b.append(s.find('span', {'class': "a-offscreen"}).text)
                df1 = pd.DataFrame([b], columns=[a])
                df = pd.concat([df, df1], axis=0, ignore_index=True)
                z+=1
                if z == len(se):
                    break
            except:
                pass

    except:
        pass

    if c == 19:
      break
    v+=1
df
df.to_excel('Data.xlsx', index=False)