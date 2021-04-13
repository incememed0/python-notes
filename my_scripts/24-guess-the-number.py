# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
import random
import time

try:
    tahmin=int(input("0-30 arası deger giriniz: "))
    sefer=1
    if tahmin>30 or tahmin<0:
        print(f"{tahmin} değeri sınırların dışında lütfen 0-30 arasında bir sayı giriniz.")
    else:
        while True:
            sayi = random.randint(0, 30)
            if tahmin==sayi:
                print(f"{sefer}.seferde tahmin edildi. {sayi}={tahmin}")
                break
            else:
                print(f"{sayi}=/{tahmin}")
            sefer+=1
            time.sleep(0.5)

except ValueError:
    print("HATA! SAYI GİR!")