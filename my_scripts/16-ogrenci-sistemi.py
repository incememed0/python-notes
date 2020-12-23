# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
#
def nothesapla(satir):
    satir=satir[:-1]
    liste=satir.split(":")
    ogrenciadi=liste[0]
    ogrencinotu=liste[1].split(',')
    not1=int(ogrencinotu[0])
    not2=int(ogrencinotu[1])
    not3=int(ogrencinotu[2])
    ortalama=(not1+not2+not3)/3
    return ogrenciadi,":",ortalama,"\n"
def notoku():
    with open("ogrenci-notlari.txt","r",encoding="utf-8") as dosya:
        for satir in dosya:
            print(nothesapla(satir))
def notgir():
    ad=input("isim: ")
    soyad = input("soyad: ")
    not1 = input("not1: ")
    not2 = input("not2: ")
    not3 = input("not3: ")
    with open("ogrenci-notlari.txt","a",encoding="utf-8") as dosya:
        dosya.write("{0} {1}: {2},{3},{4}\n".format(ad,soyad,not1,not2,not3))
def notkayit():
    with open("ogrenci-notlari.txt","r",encoding="utf-8") as dosya:
        liste=[]
        for i in dosya:
            liste.append(nothesapla(i))
        with open("sonuclar.txt","w",encoding="utf-8") as file:
            for i in liste:
                file.write(i)
while True:
    try:
        islem=int(input("1-notları oku\n"
                    "2-not gir\n"
                    "3-notları kayıt et\n"
                    "4-Çıkış\n"
                    "ne yapmak istiyorsun? : "))
        if islem==1:
            notoku()
        elif islem==2:
            notgir()
        elif islem==3:
            notkayit()
        else:
            print("programdan çıkılıyor")
            break
    except Exception as hata:
        print(f"hatalı giriş yaptınız. Tekrar deneyin.{hata}\n")
