# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
#x=10
#if x>5:
#    raise Exception("x 5den büyük deger alamaz") # Exception: x 5den büyük deger alamaz
######
def parola_kontrol(parola):
    import re
    if len(parola)<8:
        raise Exception("parola 8 harfden küçük olamaz.")
    elif not re.search("[a-z]",parola):
        raise Exception("parola küçük harf içermelidir.")
    elif not re.search("[A-Z]",parola):
        raise Exception("parola BÜYÜK harf içermelidir.")
    elif not re.search("[0-9]",parola):
        raise Exception("parola RAKAM içermelidir.")
    elif re.search("\s",parola):
        raise Exception("parola boşluk içermemelidir.")
sifre="12345mEz"
try:
    parola_kontrol(sifre)
except Exception as hata:
    print("hata sebebi: ",hata)
else:
    print(f"bu parolayı kullanabilirsin ---> {sifre}")
finally:
    print("şifreni kimseyle paylaşma")