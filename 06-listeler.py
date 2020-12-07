# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# Liste Oluşturma
liste= [1,2,"kelime",3.14,"kanada","avustralya",100,200,300]
print("liste: ",liste)
print("listenin tipi: ",type(liste))
print("listedeki eleman sayısı",len(liste))
# Boş liste oluşturmak için;
bos=[] # boş liste
print("boş küme: ",bos)
#
bosliste=list()
print("boş küme",bosliste)
# Girilen kelimenin her harfini liste şeklinde yazmak için;
m=list("merhaba")
print("girilen kelimenin her harfini liste şeklinde yazdırılması: ",m)
print("eleman sayısı: ",len(m))
print("-------------",liste,"--------------")
# Listeleri indeksleme ve parçalama
print("1.eleman: ",liste[0])
print("3.eleman: ",liste[2])
print("Sonuncu eleman: ",liste[-1])
print("1.eleman: ",liste[len(liste)-1])
print("Baştan 4. elemana kadar: ",liste[:4])
print("1-5 arasındaki elemanlar: ",liste[1:5])
print("5'den son elemana kadar: ",liste[5:])
print("2 şer atlayarak elemanlar",liste[::2])
print("elemanların tersden listelenmesi: ",liste[::-1])
print("------------ temel liste metodları ---------------")
liste1=[1,"iki",3]
liste2=["bir",2,"üç"]
liste3=liste1+liste2
print("Listelerde toplama: ",liste3)
liste1[2]="yeni"
print("listede eleman değiştirme: ",liste1)
print(liste1*3)
print("--------------------------------------------")
# append metodu, verdiğimiz değeri listeye eklememizi sağlar.
liste=[3,4,5,6]
print("liste: ",liste)
liste.append("yedi")
print("listeye eleman ekleme: ",liste)
# Elemanları değiştirme
liste[:2]=[10,11]
print("listedeki ilk 2 eleman değiştirildi: ",liste)
# pop metodu, listeden eleman çıkarır. (parantez içine değer girmezsen İNDEKS numarasına denk gelen elemanı çıkarır.)
liste.pop()
print("son eleman çıkarıldı: ",liste)
liste.pop(3) # 3. indekste "6" var. onu çıkardık.
print("3.indeksteki eleman çıkarıldı: ",liste)
# sort medotu, listedeki elemanları sıralar
liste=[5,1,13,97,33,64,23,7] # Sayı değilde kelimeler olsaydı, alfabetik sıralanırdı.
liste.sort() # Sıralar
print("listedeki değerler sıralanır: ",liste)
liste.sort(reverse=True) #listeyi tersden sıralar
print("listedeki değerler tersden sıralandı: ",liste)
print("--------------------------------------------")
# Liste içinde liste
liste=[[1,2],[3,4],[5,6]]
print(liste[1]) # [3,4]
print(liste[1][1]) # 4
# ağ yapıları kurduğumuz zaman iç içe listeler sıklıkla kullanılıyor.




