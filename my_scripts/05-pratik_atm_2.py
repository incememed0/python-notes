# author: Ercan Atar
# linkedin.com/in/ercanatar/
#################################################
# atm'den para çekme ve yatırma işlemi yapma programı
print('''
ATM programı
1.bakiyeni öğren
2.para çekme
3.para yatırma
**
çıkmak için "q" basınız.
''')
para=1000
while True:
	islem=input("Ne yapmak istersiniz? : ")
	if islem=="1":
		print("bakiyeniz: ",para)
	elif islem=="2":
		miktar=int(input("miktar giriniz: "))
		para=miktar+para
		print("son bakiyeniz: ",para)
	elif islem=="3":
		miktar=int(input("miktar giriniz: "))
		para=para-miktar
		print("son bakiyeniz: ",para)
	elif islem=="q":
		print("programdan çıkılıyor")
		break
	else:
		print("hatalı giriş yaptınız.")
