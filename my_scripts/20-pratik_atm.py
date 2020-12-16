# author: Ercan Atar
# linkedin.com/in/ercanatar/
#################################################
# Girilen bakiyeye göre 200,100,50,20 ve 10 tl'lik banknot veren program


para=int(input("Para miktarı giriniz: "))
if para/200>=1:
	adet=int(para/200)
	print(f"200tl'lik banknottan {adet} adet var.")
	para=para-adet*200
if para/100>=1:
        adet=int(para/100)
        print(f"100tl'lik banknottan {adet} adet var.")
        para=para-adet*100
if para/50>=1:
        adet=int(para/50)
        print(f"50tl'lik banknottan {adet} adet var.")
        para=para-adet*50
if para/20>=1:
        adet=int(para/20)
        print(f"20tl'lik banknottan {adet} adet var.")
        para=para-adet*20
if para/10>=1:
        adet=int(para/10)
        print(f"10tl'lik banknottan {adet} adet var.")
        para=para-adet*10
print("bozuk para: ",para)
