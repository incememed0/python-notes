# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# lambda : Kısa bir fonksiyon işlemi için fonksiyon tanımlamak yerine,bunun için bu operatör kullanılır.
# map : listeyi fonkiyona yönlendirir
# filter : lambdaya benzer ama kendi içinde bir koşul ifadesi olabilir
# return : fonksiyonun işi bittikten sonra çağırıldığı yere döndürmesidir
def karesi(sayi): return sayi**2
liste=[2,3,5,7,8,9,10]
degisken=list(map(karesi,liste))
print(degisken)
#
deger=list(map(lambda rakam:rakam**3,liste)) # kod bloklarını kısaltmak için kullan
print(deger)
#
kare=lambda ifade:ifade**2
print(kare(5)) # 5in karesi
#
def kup(sayi): return sayi%2==0
degisken=list(filter(kup,liste))
print(degisken) # çift sayıları çıktı verir
#
degisken=list(filter(lambda number:number%2==0,liste))
print(degisken)
################################
# global ve local meselesi
x="global x"
def fonkisyon():
    x="local x"
    print(x)
fonkisyon()
print(x)
#
print("------------------")
name="global string"
def greeting():
    #name="memed"
    def hello():
        #name="ercan"
        print("hello",name)
    hello()
greeting()
#
x=50
def test(x):
    #global x
    print("değer: ",x)
    x=100
    print("değişen deger: ",x)
test(x)
print(x)
#
x=50
def test():
    global x
    print("değer: ",x)
    x=100
    print("değişen deger: ",x)
test()
print(x)