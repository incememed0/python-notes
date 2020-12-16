# author: Ercan Atar
# linkedin.com/in/ercanatar/
#################################################
# metod: python kütüphanesinde tanımlanmış ulaşılabilir komutlardır.
# liste= [1,2,3,4]
# liste.append(5) ---> bu bir metoddur. noktadan sonra getirdiğimiz herşey metoddur.
# fonksiyon: metod gibi belli amaçlarayönelik olarak oluşturulmuş yapılardır.
# class: bünyesinde birçok metod bulunduran yapı
def sayhello():
    print("hello")
sayhello()
#
def merhaba(name):
    print(f"merhaba, {name}")
merhaba("ercan")
#
def merhaba1(name="user"): # parametre belirtilmediği takdirde "user" yazısı çıkacak.
    print(f"merhaba, {name}")
merhaba1()
#
def merhaba2(name="user"):
    return "hello",name
mesaj=merhaba2("ercan")
print(mesaj)
#
def sayi(num1,num2):
    return num1+num2
degisken=sayi(4,12)
print(degisken)
#
def yashesapla(dogumyili):
    return 2020-dogumyili
kisi1=yashesapla(1998)
kisi2=yashesapla(1980)
kisi3=yashesapla(2004)
print(kisi1,kisi2,kisi3)
#
def emeklilik(dogumyili2,isim):
    '''
    DOCSTRING: doğum yılınıza göre emekliliğinize kalan yıl.
    INPUT: doğum yılı , isim
    OUTPUT: hesaplanan yıl bilgisi
    '''
    yas=yashesapla(dogumyili2) # diğer fonksiyonlarla bağlantılı
    emek=65-yas
    if emek>0:
        print(f"emekliliğinize {emek} yıl kaldı")
    else:
        print("emekli oldunuz.")
emeklilik(1960,"memed")
emeklilik(1950,"memed")
print(help(emeklilik)) # fonksiyonun nasıl çalıştığına dair bilgilendirme yazabilirsin.
#
print("-----------------")
def changename(n):
    n="memed"
name="ercan"
changename(name)
print(name)
#
def change(sehir):
    sehir[0]="istanbul" # listedeki sıfırıncı değeri değiştirdik.
sehirler=["ankara","izmir"]
change(sehirler)
print(sehirler)
#
def topla(a,b,c=0):
    return sum((a,b,c))
print(topla(20,30))
print(topla(20,30,40))
#
def topla2(*parametreler): # *args
    print(type(parametreler))
    return sum((parametreler))
print(topla2(10,20,30,10,50,70))
#
print("------------------")
def displayuser(**arguman): # **kwargs
    print(type(arguman))
    for key, value in arguman.items():
        print(f"{key} is {value}")
displayuser(name="memed",age=12,city="istanbul")
displayuser(name="ercan",age=40,email="test@gmail.com")
print("------------------------")
# '*' şeklinde tanımlarsan parametre sayısını belirtmemiş olursun. # tuple listesi göndermek istiyorsan '*'
# Eğer sözlük(dictory) göndermek istiyorsan '**' şeklinde kullanıcaz.
def myfunc(a,b,*args,**kwargs):
    print(a)
    print(type(b),b)
    print(type(args),args)
    print(type(kwargs),kwargs)
myfunc(10,20,30,40,50,anahtar="ifade1",anahtar2="ifade2")