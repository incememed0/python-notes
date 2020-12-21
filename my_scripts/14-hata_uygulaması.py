# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# 1. Liste elemanları içindeki sayısal değerleri bulunuz
#liste=["10","a2","aa","20",30]
#for i in liste:
#    try:
#        degisken=int(i)
#        print(degisken)
#    except Exception:
#        continue
###########################
# 2. Kullanıcı 'q' harfine basmadığı sürece kullanıcıdan her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın
#while True:
#    sayi=input("sayi giriniz: ")
#    if sayi=="q":
#        print("programdan çıkılıyor")
#        break
#    try:
#        sayi=int(sayi)
#        print(sayi)
#    except Exception as hata:
#        print("HATAAA")
#        continue
########################
# 3. Girilen parola içinde türkçe karakter hatası veriniz.
#def parola_kontrol(parola):
#    turkce_karakter="ğĞüÜşŞöÖçÇıİ"
#    for i in parola:
#        if i in turkce_karakter:
#            raise Exception("parola içerisinde TÜRKÇE karakter olmamalı")
#        else:
#            pass
#    print("geçerli parola")
#parola=input("şifre giriniz: ")
#try:
#    parola_kontrol(parola)
#except Exception as hata:
#    print("HATA")
#################################
# 4. faktöriyel fonksiyonu oluşturup fonksiyona gelen değerler için hata mesajları verin.
from math import factorial
def kontrol(sayi):
    print(factorial(sayi))
try:
    sayi=int(input("sayi giriniz: "))
    kontrol(sayi)
except Exception as hata:
    print("HATA")
