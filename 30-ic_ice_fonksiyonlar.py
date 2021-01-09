# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
###
#def greeting(name):
#    print("hello",name)
#print(greeting("memed"))
#print(greeting)
#sayHello=greeting
#print(sayHello)
#print(greeting) # 2 adresde aynı
#print(greeting("memed"))
#print(sayHello("ali"))
#del sayHello
#print(sayHello)
#print(greeting)   #### burada dikkat etmen gereken şey; bir tanımlama yapıldığında bu Adreste yer edinir, silme işlemi yapsan bile bu adres silinmez
####################
# encapsulation
#def outer(num1):
#    print("outer")
#    def inner(sayi1):
#        print("inner")
#        return sayi1+1
#    num2=inner(num1)
#    print(num1,num2)
#outer(10)
# inner(10) iç içe fonksiyonlarda içerdeki fonksiyonu kullanamayız
###############
def factorial(number):
    if not isinstance(number,int):
        raise TypeError("gönderilen bilgi integer olmalı")
    if not number >=0:
        raise ValueError("negatif sayı veya sıfır olamaz")
    def inner_factorial(number):
        if number<=1:
            return 1
        return number*inner_factorial(number-1)
    return inner_factorial(number)
try:
    print(factorial(-9))
except Exception as hata:
    print(hata)
##############################
# burada öğrenmen gereken husus içerdeki fonksiyona erişebiliyor olmak
def us_alma(number):
    def inner(power):
        return number**power
    return inner
two=us_alma(2)
three=us_alma(3)

print(two(3)) # 2^3 = 8
print(three(4)) # 3^4 = 81
####################
def yetki(page):
    def iceri(role):
        if role=="admin":
            return f"{role} rolü {page} sayfasına ulaşabilir."
        else:
            return f"{role} rolü {page} sayfasına ULAŞAMAZ."
    return iceri
user1=yetki("product edit") # page kısmı
print(user1("admin"))
####################
def islem(islemadi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    if islemadi=="toplama":
        return toplam
    else:
        return carpma
toplama=islem("toplama")
print(toplama(1,2,3,4))
####################
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b
def issslem(f1,f2,f3,f4,islemadi):
    if islemadi=="toplama":
        print(f1(2,4))
    elif islemadi=="cikarma":
        print(f2(5,3))
    elif islemadi=="carpma":
        print(f3(3,4))
    elif islemadi=="bolme":
        print(f4(12,2))
    else:
        print("hataaaaaa")
issslem(toplama,cikarma,carpma,bolme,"toplama")
##################################
print("------------------")
##################################
# decorators fonksiyonları: bir fonksiyona özellik eklemek istediğimizde kullanırız
# bir tane decorator fonksiyonu oluşturduktan sonra diğer fonksiyonları rahatlıkla eşleştirebiliyoruz.
def my_decorator(fuck):
    def wrapper(name):
        print("fonksiyondan önceki işlemler")
        fuck(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper
@my_decorator # fonksiyondan önce olması önemli
def hello(name):     # bu fonksiyon diğer fonksiyonlara özellik eklememizi sağlıyor
    print("hello",name)
# hello=my_decorator(hello)
hello("memed")
##################################
print("------------------")
##################################
# decorator:
import math
import time

def zaman_hesapla(fuck):
    def iceri(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        fuck(*args, **kwargs)
        finish = time.time()
        print(f"fonksiyon {str(finish - start)} saniye sürdü.")
    return iceri

@zaman_hesapla
def ussu_bulma(a,b):
    print(math.pow(a,b))

@zaman_hesapla
def faktoriyel(num):
    print(math.factorial(num))

ussu_bulma(2,3)
faktoriyel(4)