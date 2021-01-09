# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
# işletim sisteminden bilgi talebi veya klasör dosya işlemleri için kullanılır
import os
import datetime
degisken=dir(os) # os kütüphanesine ait kullanılabilir metodlar
degisken=os.name # işletim sistemini verir nt:windows
degisken=os.getcwd() # dosyanın hangi klasör içerisinde olduğunu çıktı verir
#os.mkdir("dizin") # bulunduğun dizinde klasör oluşturur
#os.chdir("D:\\") # d dizin değiştirme
#degisken=os.listdir() # bulunduğu yerdeki dizinleri ve dosyaları listeler
#degisken=os.listdir("C:\\") # C dizininin altındaki dosyaları listeler
for dosya in os.listdir("C:/Users/ercan/PycharmProjects/python-notlar"):
    if dosya.endswith(".py"): # sadece .py uzantılı dosyaları listeler
        pass
        #print(dosya)
degisken=os.stat("modül2.PNG") # dosya veya dizin hakkında bilgileri çıktı verir. boyut, dosyaya son erişme zamanı ...vb.
#degisken=degisken.st_size/1024 # KB cinsinden boyut bilgisi verir
#degisken=datetime.datetime.fromtimestamp(degisken.st_ctime) # dosyanın oluşturulma tarihi
#degisken=datetime.datetime.fromtimestamp(degisken.st_atime) # son erişim tarihi
#degisken=datetime.datetime.fromtimestamp(degisken.st_mtime) # değiştirilme tarihi
# print(degisken)
####################################
# istediğimiz programı çalıştırma
#os.system("Discord.lnk") # istediğin bir programı çalıştırabilirsin
#os.rename("dizin","yenidizin") # dizin adı değişikliği
####################################
# path
degisken=os.path.abspath("21-modüller.py") # dosyanın tam dosya yolunu çıktı verir
degisken=os.path.dirname("C:/Users/ercan/PycharmProjects/python-notlar/modül-os.py") # dosya yolunu alıp sana dosya adını çıktı verir
degisken=os.path.exists("dosya-yonetimi.txt") # dosya o konumda var mı yok mu onun çıktısını verir True, False
print(degisken)

