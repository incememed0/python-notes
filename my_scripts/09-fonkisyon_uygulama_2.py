# author: Ercan Atar
# linkedin.com/in/ercanatar/
#################################################
# kendine gönderilen sınırsız sayıdaki parametreyi listeleyen fonksiyon
def cevir(*args):
    liste=[]
    for i in args:
        liste.append(i)
    return liste
degisken=cevir(10,20,30,"merhaba",100)
print(degisken)