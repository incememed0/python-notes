# author: Ercan Atar
# linkedin.com/in/ercanatar/
#################################################
# gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yaz.
def fonksiyon():
    kelime=input("gönderilen kelime: ")
    deger=int(input("kaç kez: "))
    for i in range(1,deger+1):
        print(f"belirtilen kelime {kelime}'dir.")
fonksiyon()
#
def yaz(kelime,adet):
    print(kelime*adet)
yaz("merhaba\n",4)