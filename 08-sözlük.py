# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# Sözlük oluşturma
#	anahtar
#	  ||
#	  \/
sozluk={"sıfır":"zero","bir":1,2:"two",3:3}
print(type(sozluk),sozluk)
# Boş sözlük için;
sozluk2={}
sozluk3=dict()
print(sozluk["sıfır"])
# Sözlüğe ekleme-çıkarma
sozluk["dört"]="four" #ekleme
print(sozluk)
sozluk["dört"]=4 # değiştirme
print(sozluk)
print("--------------------------------")
# sözlüklerde indeks kavramı bulunmamaktadır.
a = {"bir":[1,2,3,4],"iki":[[1,2],[3,4],[5,6]],"üç":15}
print(a)
print(a["iki"]) # [[1,2],[3,4],[5,6]]
print(a["iki"][1]) # [3,4]
print(a["iki"][1][1]) # 4
# iç içe sözlükler

