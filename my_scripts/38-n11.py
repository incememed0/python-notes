# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
import requests
from bs4 import BeautifulSoup

url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html=requests.get(url).content
soup=BeautifulSoup(html,"html.parser")
liste=soup.find_all("li",{"class":"column"},limit=10)
for li in liste:
    name=li.div.a.h3.text.strip()
    link=li.div.a.get("href")
    eskifiyat=li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
    yenifiyat=li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip("TL")
    print(f"ürün: {name} , linki: {link} , fiyatı: {yenifiyat}")