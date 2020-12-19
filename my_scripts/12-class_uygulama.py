# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
#
class Sorular:
    def __init__(self,soru,sik,cevap):
        self.soru=soru
        self.sik=sik
        self.cevap=cevap
    def kontrolet(self,cevap):
        return self.cevap==cevap
class Sinav:
    def __init__(self,soru):
        self.soru=soru
        self.puan=0
        self.soruindex=1

soru1=Sorular("en iyi programlama dili hangisidir?",["Ruby","Python","C++","Java"],"Python")
soru2=Sorular("en popüler programlama dili hangisidir?",["Ruby","Python","C++","Java"],"Python")
soru3=Sorular("en çok kazandıran programlama dili hangisidir?",["Ruby","Python","C++","Java"],"Python")
liste=[soru1,soru2,soru3]

sinav=Sinav(liste)
soru=sinav.soru[sinav.soruindex]
print(soru.soru)

################## sonra devam et