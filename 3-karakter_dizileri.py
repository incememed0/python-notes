# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# String oluşturmak için 3 farklı yol mevcut;
print('tek tırnaklı')
print("çift tırnaklı")
print("""üç çift tırnaklı""")
print('''üç tek tırnaklı''')
print("--------- \ detayı ---------")
print("Ercan'ın bugün dersi var.")
print('Ercan\'ın yarında dersi var.') # " \ " işareti ile tek tırnakla ilgili hatalardan kurtulabilirsin.
print("----------------------------")
#
degisken="bir cümle, bir değişkene atanabilir."
print(degisken)
# String indeksleme ve parçalama
# indexlerde dikkat etmen gereken; ilk harf SIFIR'ıncı indextir. Değişken diye tanımladığım cümlede
# b:0 - i:1 - r:2 - (boşluk):3 - c:4 - ü:5 - m:6 - l:7 ...
#
print(degisken[0]) # b
print(degisken[1]) # i
print(degisken[2]) # r
print(degisken[3]) #
print(degisken[4]) # c
print("----")
print(degisken[-4]) # l
print(degisken[-3]) # i
print(degisken[-2]) # r
print(degisken[-1]) # .
print("----") # İndex parçalama ---> degisken[başlama_indeksi:bitiş_indeksi:atlama_değeri]
print(degisken[5:10:1]) # ümle,
print(degisken[:10]) # bir cümle,
print(degisken[5:]) # ümle, bir değişkene atanabilir.
print(degisken[:]) # bir cümle, bir değişkene atanabilir.
print(degisken[:-4]) # bir cümle, bir değişkene atanabi
print(degisken[::-1]) # Bütün cümleyi tersden çıktı verir.
print("---------------------------")
###################################################
# String özellikleri;
# atanmış olan değişkeni kullanıcam.
degisken_sayisi=len(degisken) # Değişkendeki karakter sayısını çıktı verir.
print(degisken_sayisi)
# Stringler değiştirilemez.
# kelimeleri toplama işlemiyle yan yana yazabilirsin.
a="merhaba"
b="dünya,"
c="ben"
d="ercan"
print(a+b+c+d)
d=b
c=a
print(a+b+c+d)
print(a*3)
# String değiştirilmiyor amaaaa üzerine yazarak değiştirebilirsin.
print(a)
a=a+"ERCAN"
print(a)
###################################################
