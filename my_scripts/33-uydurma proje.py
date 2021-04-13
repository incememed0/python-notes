# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################

import time

neicin=input("Ne için alarm kuruyorsun: ")
alarm=input("(sa:dk:sn şeklinde saat giriniz)\nne zamana alarm kurayım: ")

while True:
    degisken=time.strftime('%X')
    time.sleep(1)
    if alarm==degisken:
        print(f"{neicin} için zaman geldi!")
        break

"""

%a:  hafta gününün kısaltılmış adı
%A:  hafta gününün tam adı
%b:  ayın kısaltılmış adı
%B:  ayın tam adı
%c:  tam tarih, saat ve zaman bilgisi
%d:  sayı değerli bir karakter dizisi olarak gün
%j:  belli bir tarihin, yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı
%m:  sayı değerli bir karakter dizisi olarak ay
%U:  belli bir tarihin yılın kaçıncı haftasına geldiğini gösteren 0-53 arası bir sayı
%y:  yılın son iki rakamı
%Y:  yılın dört haneli tam hali
%x:  tam tarih bilgisi
%X:  tam saat bilgisi

"""