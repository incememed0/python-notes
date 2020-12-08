# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
demet=(1,2,3,4,5)
print(type(demet))
print("Demetin elemanları: ",demet)
print("Demetin 1.elemanı: ",demet[1])
print("Demetin son elemanı: ",demet[-1])
# Listeler ile birebir benzerlik taşır aradaki tek fark demetler değiştirilemez.
print(demet[::-1])
print("-----------------------")
# demetlerde 2 metod bulunur;
# index metodu
demet=("merhaba",100,200,"marmaris","bodrum",300)
print("index metodu: ",demet.index("marmaris")) # index değerini çıktı verir. --> 3
# count metodu
demet=(1,1,1,1,2,3,4,3,5,5,5,"m","m")
print("count metodu: ",demet.count(1)) # demetin içerisinde bir ifade kaç defa geçtiğini çıktı verir.
# Demetler ne zaman kullanılır?
# Demetler çok sıklıkla kullanılmaz temel özelliği değiştirilemez olmasıdır.
