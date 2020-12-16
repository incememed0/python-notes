# author: Ercan Atar
# linkedin.com/in/ercanatar/
#################################################
# asal sayı bulma
# girilen sayının asal olup olmadığını kontrol edem program
while True:
    asal=True
    sayi=int(input("sayı: "))
    if sayi==1:
        print("1 asal değildir.")
    for i in range(2,sayi):
        if sayi%i==0:
            asal=False
            break
    if asal:
        print("sayı asaldır")
    else:
        print("asal değildir.")