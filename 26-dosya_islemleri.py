# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# dosya açmak ve oluşturmak için open() fonksiyonu kullanırız
# kullanımı: open(dosya_adı,dosya_erişme_modu)
# dosya_erişme_modu ---> dosyayı hangi amaçla açtığını belirtir.
################
# w ---> Üstüne yazar
# a ---> yazı ekler
# x ---> dosya oluşturur. (varsa hata verir)
# r ---> dosya okuma
#####################
#dosya=open("C:/Users/ercan/Documents/dosya.txt","w",encoding="utf-8")
#dosya.write("merhaba")
#dosya.close() # dosyayı mutlaka kapatmayı unutma. bellekte yer kaplar.
###############
#dosya=open("C:/Users/ercan/Documents/dosya.txt","a",encoding="utf-8")
#dosya.write("merhaba\n")
#dosya.close() # dosyayı mutlaka kapatmayı unutma. bellekte yer kaplar.
#################
#dosya=open("C:/Users/ercan/Documents/dosya3.txt","x")
#dosya.close()
##########
#dosya=open("dosya-yonetimi.txt","r",encoding="utf-8") # türkçe karakterleri okuya bilmek için encoding ekledik
### 3 yöntem ile çıktı alınır
# 1.yöntem
#for i in dosya:
#    print(i,end="") # araya boş satır eklemeden çıktı almak için end="" ekledik
##
#2.yöntem
#cıktı=dosya.read()
#print(cıktı)
##
#3.yöntem
#print(dosya.read())
##### imleç dosya ilk okuduğu sırada en baştan itibaren okumaya başlar
#cıktı1=dosya.read()
#print("-- 1.çıktı --")
#print(cıktı1)
#dosya=open("dosya-yonetimi.txt","r",encoding="utf-8") #     <--------------------------------------
#cıktı2=dosya.read()                 #                                                              |
#print("-- 2.çıktı --")                                             #                               |
#print(cıktı2) # ama burada tekrar çıktı istediğimizde çıktı en sonra olduğu ve dosya.close()       |
# yapmadığımız için veya dosyayı tekrar açmadığımız için imleç en sondadır. ve çıktı vermez   ------
#dosya.close()
##########
#cıktı=dosya.read(10) # sayı belirtisen ilk 10 karakteri çıktı verir
#print(cıktı)
#cıktı=dosya.read(3)
#print(cıktı)
#cıktı=dosya.read(4)
#print(cıktı)
#dosya.close()
#----------### readline()
#dosya=open("dosya-yonetimi.txt","r",encoding="utf-8")
#print(dosya.readline(),end="") # ilk satırı okur end eklemeyi unutma
#print(dosya.readline())
#print(dosya.readline())
#dosya.close()
##--- readlines()
#dosya=open("dosya-yonetimi.txt","r",encoding="utf-8")
#print(dosya.readlines()) # ['merhaba\n', '2.satır\n', '3.satır\n', 'yeni metin\n', '123456'] şeklinde çıktı verir
#cıktı=dosya.readlines()
#print(cıktı[3]) # 3. satırdaki yazıyı çıktı verir
#dosya.close()
#------------#------------------------------------------------------------------------------------#--------------------#
# fonksiyon meselesi
# with ile işlemleri fonksiyon haline getirip coddan tasarruf yapıyoruz. böylelikle close() işlemine ihtiyacımız yok
with open("dosya-yonetimi.txt","r",encoding="utf-8") as dosya:
    cikti=dosya.read()
    print(cikti)
    print("--------")
    dosya.seek(5) # imleci istediğin yere konumlandırır   #  imleci 5.harfin önüne konumlandırır.
    print(dosya.tell()) # imlecin konumunu belirtir.
    print("---------")
    cikti2=dosya.read()
    print(cikti2)