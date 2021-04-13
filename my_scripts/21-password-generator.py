# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
import random

harfverakam="qwertyuıopğüasdfghjklşi,zxcvbnmöç.0123456789"
def program():
    adet=int(input("kaç adet şifre istersin: "))
    uzunluk=int(input("şifre uzunluğu: "))
    print("şifre seçenekleriniz;")
    for pwd in range(adet):
        sifre=""
        for c in range(uzunluk):
            sifre+=random.choice(harfverakam)
        print(sifre)

try:
    program()
except ValueError:
    print("HATA! PROGRAMI TEKRAR ÇALIŞTIR VE SAYI GİR!")