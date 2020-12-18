# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# class: bizim için daha önceden oluşturulmuş ve belli başlı bazı özellikler ve belli başlı bazı metodlar class içerisine aktarılmıştır.
# instance (object=obje)
# self: oluşturulan ifadeyi temsil ediyor. self yerine başka isimde verebilirsin.--> örn: p1
#########################################################
# class İsim:                                           #
#   class attributes                                    # attributes:
#   def __init__(self): --> constructor(yapıcı metod)   # --> init metodu, oluşturulan her bir obje için çalıştırılıyor olması lazım
#       self.isim=ad   --> object attributes            #
#       self.yas=sayi  --> object attributes            #
#                                                       #
#   def giris(self): --> instance methods               #
#                                                       #
#########################################################
# liste1=[1,2,3]
# liste2=[1,2,3,4,5]
# liste1.append() # noktadan sonraki metodların hepsini oluşturduğum obje üzerinden kullanabilirim
class Person:
    adres="bilgi girilmedi."
    def __init__(self,name,year):
        self.name=name
        self.birthyear=year
        print("init metodu çalıştırıldı.")
    def intro(self):
        print(f"merhaba, {self.name}")
    def hesapla(self):
        return 2020-self.birthyear
p1=Person(name="memed",year=1990)
p2=Person("cabbar",2000)
print(p1)
print(p2)
print(type(p1))
print(p1==p2)
print("------------------")
print(f"isim: {p1.name} , doğum tarihi: {p1.birthyear} , adres: {p1.adres}")
p1.name="ahmet" # class içerisindeki bilgiyi değiştirebilir veya ekleyebilirim.
p1.adres="türkiye/istanbul"
print(f"isim: {p1.name} , doğum tarihi: {p1.birthyear} , adres: {p1.adres}")
print("------------------")
p1.intro()
p2.intro()
print(f"{p1.hesapla()}")
print("------------------")
# inheritance(kalıtım): başka bir class'ı işaret ederek onun özelliklerinin kazanılması
class Teacher():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print("teacher")
    def whoami(self):
        print("i am a teacher")
    def eat(self):
        print("teacher")
class Student(Teacher):
    def __init__(self,fname,lname):
        Teacher.__init__(self,fname,lname)
        print("student")
    def eat(self): # aynı isme ait bir fonksiyon var ise öbürünü ezer. (override)
        print("student")
t1=Teacher("ali","yılmaz")
s1=Student("memed","ince")
print(t1.firstname,"*",t1.lastname)
print(s1.firstname,"-",s1.lastname)
t1.whoami() #
s1.whoami() # aynı fonksiyona ulaşabiliyorum
t1.eat()
s1.eat()