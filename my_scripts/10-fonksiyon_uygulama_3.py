# author: Ercan Atar
# linkedin.com/in/ercanatar/
#################################################
# bankamatik
hesapA={
    'ad':'memed',
    'hesapno':'123456',
    'bakiye':3000,
    'ekhesap':2000
} # sözlük tipinde bilgiler işleniyor.
hesapB={
    'ad':'cabbar',
    'hesapno':'654321',
    'bakiye':2000,
    'ekhesap':1000
}
def paracek(hesap,miktar):
    print(f"merhaba {hesap['ad']}")
    if hesap['bakiye']>=miktar:
        hesap['bakiye']-=miktar
        print("paranızı alabilirsiniz.")
        bakiyesorgula(hesap)
    else:
        toplam=hesap['bakiye']+hesap['ekhesap']
        if (toplam>=miktar):
            ekhesapkullanimi=input("ek hesap kullanılsın mı? (e/h) : ")
            if ekhesapkullanimi=="e":
                ekhesapkullanilacakmiktar=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekhesap']-=ekhesapkullanilacakmiktar
                print("paranızı alabilirsiniz")
                bakiyesorgula(hesap)
            else:
                print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("üzgünüm, bakiyeniz yetersiz.")
            bakiyesorgula(hesap)
def bakiyesorgula(hesap):
    print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} tl bulunmaktadır. ek hesap limitiniz: {hesap['ekhesap']}")
# def parayatir(hesap,miktar):
# önce ek hesapdaki miktar dolucak ardından ana hesapdaki bakiyeyi doldurucak şekilde bir
# kod düzenlemesi yapılabilir.
paracek(hesapA,4000)
