# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# Mantıksal değerler (boolean)
# true ve false 'dan ibarettir.
dogru=True
yanlis=False
print("True ifadesi:{0} \nFalse ifadesi:{1} ".format(type(dogru),type(yanlis)))
# Bütün rasyonel sayılar True çıktısı verirken, sadece sıfır false çıktısı verir.
print("True çıktıları: ",bool(11),bool(3.14),bool(-4.3))
print("false çıktıları: ",bool(0))
print("Farklı kullanım şekilleri:",1==1,1!=1)
# Sonra atama işlemi yapmak için;
a= None
print(a)
print("-------- AND OR ---------")
# AND
print(1<2 and "a"=="a") # TRUE 1 1
print(1>2 and "a"=="a") # False 0 1
print(1>2 and "a"!="a") # False 0 0
# OR
print(1<2 or "a"=="a") # True 1 1
print(1>2 or "a"=="a") # True 0 1
print(1>2 or "a"!="a") # False 0 0
print("-------- NOT -----------") # Çıkacan değeri ters çevirir.
print(1==1)
print(not 1==1)
