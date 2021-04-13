# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################

import sys

sayi = input('Bir sayı girin: ')

if int(sayi) < 0:
    print('çıkılıyor...')
    sys.exit()

else:
    print(sayi)