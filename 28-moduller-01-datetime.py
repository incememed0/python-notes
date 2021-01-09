# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
from datetime import datetime
from datetime import timedelta
degisken=datetime.now() # .year , .day , .hour ... ekleyerek spesifik olarak belirtilen değer alır.
print(degisken)
degisken=datetime.now().ctime() # 2 farklı tarih gösterimi
print(degisken)
#######3
simdi=datetime.today()
degisken=datetime.strftime(simdi,"%Y") # yıl
degisken=datetime.strftime(simdi,"%a") # gün
degisken=datetime.strftime(simdi,"%b") # ay
degisken=datetime.strftime(simdi,"%d") # ayın kaçı olduğu
degisken=datetime.strftime(simdi,"yıl bilgisi: %Y , ay bilgisi:%B , tarih:%x") # büyük harf detaylı yazar, küçük harf ise kısa
print(degisken)
#########
tarih="21 nisan 2019"
gun,ay,yil=tarih.split()
print(gun)
print(ay)
print(yil)
#
tarih="10 November 1938 hour 09:05:30"
degisken=datetime.strptime(tarih,"%d %B %Y hour %H:%M:%S") # Bu kısım bire bir aynısı yazılmalı, hata verebilir
print(degisken)
print(degisken.year)
birtday=datetime(1999,9,9)
print(birtday) # saat belirtilmediği için 00:00:00
birtday=datetime(1999,9,9,10,10,11)
print(birtday)
degisken=datetime.timestamp(birtday) # saniye cinsinden çıktı verir
print(degisken)
degisken=datetime.fromtimestamp(degisken) # bu sefer tam tersi saniye bilgisinden tarih bilgisine çevirir
print(degisken)
degisken=datetime.fromtimestamp(0) # 1970-01-01 03:00:00
print(degisken)
zaman=birtday-degisken
print(zaman)
zaman=zaman.days
print(zaman)
####################
# gün ekleme
zaman=zaman,timedelta(days=20) # 20 gün eklenir
print(zaman)
