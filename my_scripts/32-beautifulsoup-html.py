# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
# dökümantasyon: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup

html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>merhabalar</title>
</head>
<body>
    <h1>Python Notlarım</h1>
    <div class="grup1">
    <h2>Programlama</h2>
<ul>
    <li>menü 1</li>
    <li>menü 2</li>
    <li>menü 3</li>
</ul>
    </div>
    <div class="grup2">
    <h2>Modüller</h2>
<ul>
    <li>menü.1</li>
    <li>menü.2</li>
    <li>menü.3</li>
</ul>
    </div>
    
    </div>
    <div class="grup3">
    <h2>django</h2>
<ul>
    <li>menü.11</li>
    <li>menü.22</li>
    <li>menü.33</li>
</ul>
    </div>
</body>
</html>
"""

soup=BeautifulSoup(html_doc,'html.parser')
#result=soup.prettify()
#result=soup.title
#result=soup.title.name
#result=soup.title.string
#result=soup.head
#result=soup.body

#result=soup.h1
#result=soup.h2
#result=soup.h2.name
#result=soup.h2.string

#result=soup.find_all('h2')
#result=soup.find_all('h2')[0]

#result=soup.div
#result=soup.find_all('div')[1].ul.find_all('li')

#result=soup.div.findChildren()

result=soup.div.findNextSibling().findNextSibling().findPreviousSibling()

print(result)