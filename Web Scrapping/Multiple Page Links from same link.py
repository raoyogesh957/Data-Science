import requests
from bs4 import BeautifulSoup
import urllib
# urllib.request.urlopen(url)
url = 'https://www.amazon.in/s?k=laptop&crid=2J7LCMD2BA4RR&sprefix=laptop%2Caps%2C298&ref=nb_sb_noss_1'

for i in range(5):
    print(url)
    a='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    link = requests.get(url, headers=({'User-Agent': a}))
    soup = BeautifulSoup(link.content, 'html.parser')
    clas = 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator'
    next_link = soup.find('a', {'class': clas}).get('href')
    url = 'https://amazon.in'+next_link
