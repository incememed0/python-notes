# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
print("""########################
#### Hesap Makinesi ####
########################
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
########################""")
a=int(input("birinci değer: "))
b=int(input("ikinci deger: "))
islem=input("Hangi işlemi yapalım: ")
if islem=="1":
	print("{0} ile {1}'nin toplamı {2}'dır.".format(a,b,a+b))
elif islem=="2":
	print("{0} ile {1}'nın farkı {2}'dır.".format(a,b,a-b))
elif islem=="3":
        print("{0} ile {1}'nın çarpımı {2}'dır.".format(a,b,a*b))
elif islem=="4":
        print("{0} ile {1}'nın bölümü {2}'dır.".format(a,b,a/b))
else:
	print("hatalı işlem yaptınız.")
