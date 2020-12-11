# author: Ercan Atar
# linkedin.com/in/ercanatar/
#################################################
# Break komutu sadece bulunduğu döngü içerisinden çıkmanı sağlıyor.

while True:
	for i in range(1,10): # 10 dahil değil. 1-9 yazdırıcak
		if i==5:
			print("5'e geldi")
			break
		print(i)

	print("1.mesaj")
	break
	print("2.mesaj")

print("--- continue kullanımı ---")
for i in range(1,11):
	if i==5 or i==7:
		print("---")
		continue
	print(i)
