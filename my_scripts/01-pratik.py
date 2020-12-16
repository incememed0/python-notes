# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# Kullanıcıdan 3 girdi alınıp çıktı veren program
print("Rehbere kişi kaydetme programı")
isim=input("Ad: ")
soyad=input("Soyad: ")
telefon=int(input("Telefon no: "))
demet=(isim,soyad,telefon)
print("isminiz: {0} \nsoyad: {1} \ntel: {2}".format(demet[0],demet[1],demet[2]))
