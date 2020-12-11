# author: Ercan Atar
# linkedin.com/in/ercanatar/
#################################################
liste=[1,2,3,4]
print(liste)
liste.append("yeni_eleman") # append: yeni eleman eklerken kullanılır.
print(liste)
print("------------------")
# Liste1'i liste2'ye yazdıralım.
liste1=[1,2,3,4,5]
liste2=[i for i in liste1]
print("liste2'ye yazdırdık: ",liste2)
# örnek 2
liste1 = [1,2,3,4,5]
liste2 = [i*2 for i in liste1]
print("liste1'deki elemanları 2 ile çarptık: ",liste2)
# örnek 3
liste1 = [(1,2),(3,4),(5,6)]
liste2 = [i*j for (i,j) in liste1]
print("i,j: ",liste2)
# örnek 4
liste1 = [1,2,3,4,5,6,7,8,9,10]
liste2 = [i for i in liste1 if not (i == 4 or i == 9)] # List Comprehension
print("listeden 4 ve 9'u çıkardık: ",liste2)
print("------------------")
# comprehension daha çok liste içerisinde fazla listeleri bir liste haline getirmek için kullanılıyor
# 1. örnek: uzun uzun yazılışı
liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = list()
for i in liste:
	print(i) ## Buradaki i değeri de aslında bir liste.

# list comprehension metodu
liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = [x for i in liste for x in i] # Biraz karmaşık ama çözersin. :)
print(liste2)
