# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# kullanıcıdan dosya ismi al ve içerisine kullanıcıdan aldığın verilere göre bilgileri
# al ve işlem bittikten sonra çıktı veren program
def dosyaolustur():
    isim=input("dosya ismi giriniz: ")
    dosya=open(f"{isim}.txt","x",encoding="utf-8")
    dosya.close()
def dosyayaz():
    deger=input("dosya ismini giriniz: ")
    with open(f"{deger}.txt","w",encoding="utf-8") as dosya:
        yaz=input("ne yazalım?\n: ")
        dosya.write(f"{yaz}")
def dosyaoku():
    deger=input("dosya ismini giriniz: ")
    dosya=open(f"{deger}.txt","r",encoding="utf-8")
    print(dosya.read())
    dosya.close()

def anaprogram():
    while True:
        kapatalimmi=input("devam edelim mi? (çıkış=q): ")
        if kapatalimmi=="q":
            print("program kapatılıyor.")
            break
        else:
            deger=int(input("[1-dosya oluştur]\n"
                        "[2-dosyayı yaz]\n"
                        "[3-dosyayı oku]\n"
                        "hangi işlemi yapalım?: "))
            if deger==1:
                dosyaolustur()
            elif deger==2:
                dosyayaz()
            elif deger==3:
                dosyaoku()
            else:
                print("hatalı giriş yaptınız.")

anaprogram()