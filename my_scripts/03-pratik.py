# author: Ercan Atar
# linkedin.com/in/ercanatar/
#################################################
# kullanıcıdan kullanıcı adı ve parola alıp sorgulayan bir sistem kuralım.

nick="memed"
password="1234"
giris=3

while True:
	sayi1=input("Kullanıcı adı: ")
	sayi2=input("şifre: ")
	if sayi1!=nick and sayi2==password:
		print("kullanıcı adı hatalı")
		giris-=1
	elif sayi1==nick and sayi2!=password:
		print("parola hatalı")
		giris-=1
	elif sayi1!=nick and sayi2!=password:
		print("kullanıcı adı ve şifre hatalı")
		giris-=1
	else:
		print("başarılı giriş yaptınız.")
		break
	if giris==0:
		print("giriş hakkınız bitti")
		break
