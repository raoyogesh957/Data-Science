import time
import requests
import io
import hashlib
import os
from selenium import webdriver
import webbrowser
import bs4
import urllib
import os

from selenium.webdriver.common.keys import Keys


def get_image_url(name):
    url = 'https://www.google.com/search?q='
    for i in name.strip():
        if i.isspace():
            b, c = name.split()
            name = '+'.join([b, c])
        else:
            name
    link = url + name

    r = requests.get(link, {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'})
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    for i in soup.find_all('a', {'class': 'eZt8xd'}):
        if i.text == 'Images':
            url = 'https://www.google.com/search?q={}'.format(name) + i.get('href')
            return url

def download_images(url,length):
    webdriver_path = 'C:/Users/Yogesh Yadav/Downloads/chromedriver_win32'
    driver = webdriver.Chrome(webdriver_path)
    driver.get(url)
    images = []
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)
        thumbnail_results = driver.find_elements("css selector", "img[class ='rg_i Q4LuWd']")
        for img in thumbnail_results:
            if img.get_attribute('src') and 'http' in img.get_attribute('src'):
                images.append(img.get_attribute('src'))
        if len(images)>length:
            break
    driver.quit()
    return images

def save_images(images,name):
    c = 0
    s = set()
    path = 'c:\\Users\\Yogesh Yadav\\OneDrive\\Desktop\\DS\\Python Learnings'
    try:
        os.makedirs(path + '\\'+name)
    except:
        print('Already Exist')
    os.chdir(str(path + '\\'+name))

    for i in images:

        if i[:1] == '/':
            pass
        else:
            img = i
        with open(str(c) + '.jpg', 'wb') as f:
            f.write(urllib.request.urlopen(img).read())
            f.close()
        c += 1


if __name__=='__main__':
    name='Roger Federar'
    url=get_image_url(name)
    images=download_images(url,65)
    save_images(images, name)




