# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
#			 #
# for DEĞİŞKEN in KOŞUL: #
# 	KOMUT		 #
#			 #
##########################
toplam=0
liste=[2,3,1,14,26,100]
for eleman in liste:
	toplam+=eleman
	print(f"eleman: {eleman}, Toplam: {toplam}") # print("eleman: {}, Toplam: {}".format(eleman,toplam))
print("----------------------")
# Çift elemanları bastırma
liste = [1,2,3,4,5,6,7,8,9]
for eleman in liste:
	if eleman % 2 == 0:
		print(eleman)
print("----------------------")
# Karakter dizileri üzerinde gezinmek
s =  "Python"
for karakter in s:
	print(karakter)
print("----------------------")
# Her bir karakterleri 3 ile çarpma
s = "Python"
for karakter in s:
	print(karakter * 3)
print("----------------------")
# Listelerle aynı mantık
demet =  (1,2,3,4,5,6,7)
for eleman in demet:
	print(eleman)
print("----------------------")
# Listelerin için 2 boyutlu demetler
liste = [(1,2),(3,4),(5,6),(7,8)]
for eleman in liste:
    	print(eleman) # Herbir elemanın  demet olduğu görebiliyoruz.
print("----------------------")
# Demet içindeki herbir elemanı almak için pratik yöntem
liste = [(1,2),(3,4),(5,6),(7,8)]
for (i,j) in liste:
	print("i: {} , j: {}".format(i,j))
print("----------------------")
# Demet içindeki elemanları çarpalım.
liste = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for (i,j,k) in liste:
	print(i * j * k)
print("---------- sözlükler ------------")
# Sözlük yapılarında sıklıkla kullanıyoruz.[ keys() , values() , items() ]
sozluk = {"bir":1,"iki":2,"üç":3,"dört":4}
print(sozluk)
for eleman in sozluk:
	print(eleman)
for eleman in sozluk.values():
	print(eleman)
for i,j in sozluk.items():
	print(i,j)
