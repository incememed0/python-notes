import requests
import time
from bs4 import BeautifulSoup

url= 'https://www.hepsiburada.com/huawei-watch-gt2-46mm-sport-akilli-saat-siyah-p-hbv00000p131l'

headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}

def check_price():
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id='product-name').get_text().strip()
    title=title[0:27]
    print(title)
    span=soup.find(id='offering-price')
    content=span.attrs.get('content')
    price=float(content)
    print(price)

check_price()

