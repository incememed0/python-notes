# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
# request: websitesi ziyaret edilmeden sayfanın kaynak kodunun alınmasında kullanılır
import requests
import json

degisken=requests.get("https://jsonplaceholder.typicode.com/todos")
degisken=json.loads(degisken.text)
#degisken=degisken.text
#print(degisken[0]["title"])
#print(type(degisken))
for i in degisken:
    if i["userId"]==1:
        print(i["title"])

