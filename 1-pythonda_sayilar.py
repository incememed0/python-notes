# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
#
3+2
8-4
print(4+9)
print(3.5+2.7)
print("--------------") # Değişkenler tanımlanarak kullanılır
toplam=12+3
print(toplam)
cikarma=32.3+12.4
print(cikarma)
print("--------------") # Üssü bu şekilde alınır. ve Değişkenin değeri değiştirilebilir.
i=10
print(i*i*i)
i=15
print(i)
print("--------------") # Denklemler kurularak yazılabilir
a=4
b=3
c=a+2*b
print(c)
print("--------------")
#	Değişkenlerimize isim verirken dikkat etmemiz gereken noktalar;
#1. Değişken isimleri bir sayı ile başlayamaz.
#2. Değişken ismi kelimelerden oluşuyorsa aralarında boşluk olamaz.
#3. :'",<>/?|\()!@#$%^&*~-+ Buradaki semboller değişken ismi içinde kullanılamaz.(Sadece _ sembolü kullanılabilir)
#4. Pythonda tanımlı anahtar kelimeler değişken ismi olarak kullanılamaz.(while, not vs. )
#############################################
# Python'da iki değişkenin değerini birbiriyle değiştirmek için pratik bir yöntem bulunmaktadır.
a = 4
b = 3
print("a : ",a," b : ",b)
a,b = b,a
print("a : ",a," b : ",b)
print("--------------")
# Bir değişkenin değerini artırma işlemlerinde Pythonda pratik bir yöntem bulunmaktadır
a=5
a=a+1
print(a)
a+=1
print(a)
a-=4
print(a)
a*=3
print(a)
""" Yorum satırı
için 3 tırnakda
kullanılabilir"""
