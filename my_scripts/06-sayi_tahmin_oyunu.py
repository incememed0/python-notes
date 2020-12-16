# author: Ercan Atar
# linkedin.com/in/ercanatar/
#################################################
"""
sayı tahmin oyunu;

"""
import random
sayi=random.randint(1,100)
hak=int(input("Kaç sefer tahmin etmek istersiniz?: "))
sayac=0
while hak > 0:
    hak=hak-1
    sayac=sayac+1
    tahmin=int(input("bir sayı tahmin ediniz: "))
    if sayi==tahmin:
        print("Kazandınız.{} seferde bildiniz. puanınız: {}".format(sayac,100-(100/hak)*(sayac-1)))
        break
    elif sayi>tahmin:
        print("yukarıııı!")

    else:
        print("aşağı")

    if hak==0:
        print(f"hakkınız bitti. Tutulan sayı {sayi}")