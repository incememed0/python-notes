# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
# döviz türü seçicez. alınacak türü seçicez, miktarı sorucak. çıktıda ise alınacak para biriminin karşılığı gelicek

import json
import requests

api_url=f"https://api.exchangeratesapi.io/latest?base="

bozulan_doviz=input("Bozulan döviz birimi: ")
alinan_doviz=input("alınan döviz türü: ")
miktar=int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))
result=requests.get(api_url,bozulan_doviz)
result=json.loads(result.text)
print("1. {0} = {1} {2}".format(bozulan_doviz,result["rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar * result["rates"][alinan_doviz],alinan_doviz))