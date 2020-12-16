# author: Ercan Atar
# linkedin.com/in/ercanatar/
#################################################
# sayı dizisi oluşturmada kullanılan bir operatör
print("1-10 arasındaki değerler: ",*range(1,10)) # * koymazsan hata verir. # 1 2 3 ... 8 9
print("başlangıç değeri vermezsen: ",*range(10)) # 0 1 2 3 ... 8 9
print("1-20 arasında 2şer arttırarak: ",*range(1,20,2)) # 1 3 5 7 ... 15 17 19
print("tersden liste oluşturma: ",*range(10,1,-1))
print(type(range(1,10)))
print("--------------------------------")
# Aradaki fark
liste = [1,2,3,4,5,6,7]
for i in liste:
	print(i)
print("--- range ---")
#
for i in range(1,8):
	print(i)
