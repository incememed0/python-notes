# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# Tam sayıyı ondalık sayıya çevirme.
a=42
a=float(a)
print(a)

sayi1=int(12)
print(sayi1)
# Ondalık sayıyı tam sayıya çevirme.
b=4.12345
b=int(b)
print(b)

sayi2=int(23.12342342)
print(sayi2)
# Sayıları string ifadeye çevirme.
kelime=str(1234.123)
print(kelime)

# kelime uzunluğu
print(len(kelime))

# \n ---> alt satıra geç
# \t ---> 4 boşluk bırak

# değişkenin hangi veri tipine sahip olduğunun çıktısı.
print(type(kelime))
print(type(a))
print(type(b))
print("---\t---\t---\t---")
# Çoğunlukla biz bu veri tipi dönüşümlerini int --> str şeklinde kullanıyoruz.
a=12
print(type(a),a)
a=str(a)
print(type(a),a)
