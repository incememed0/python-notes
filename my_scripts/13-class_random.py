# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
import random
degisken=random.randint(1, 10) # 1-10 (1 ve 10 dahil) bütün sayılar # integer sayılar 1,2,3,4...
degisken2=random.random() # 0.0-1.0 arasındaki float sayılar # 0.12414342432 , 0.543543531
degisken3=random.uniform(1,10) # 1-10 arasında float sayılar
print(degisken)
print(degisken2)
print(degisken3)
#
harf="istanbul"
liste=["mehmet","ali","veli","ayşe","fatma","hayriye"]
isim=liste[random.randint(0,len(liste)-1)]
isim1=random.choice(liste)
harf1=random.choice(harf)
print(isim)
print(isim1)
print(harf1)
#
liste1=[1,2,3,4,5,6,7]
print(liste1)
random.shuffle(liste1) # orjinal listenin yerlerini değiştirerek kullanır
print(liste1)
#
print("-------------------")
liste2=range(100)
degisken=random.sample(liste2,3)
print(degisken)
degisken=random.sample(liste,3)
print(degisken)