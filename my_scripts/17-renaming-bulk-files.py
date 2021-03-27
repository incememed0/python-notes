# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
# dosyaların isimlerini toplu şekilde değiştirme programı
# deneme klasöründeki dosyaları metin_belgesi1.txt,metin_belgesi2.txt... şeklinde isimlendiricek.
import os

def main():
    i=1
    path="C:/Users/ercan/PycharmProjects/python-notlar/my_scripts/deneme/"
    for filename in os.listdir(path):
        my_dest="metin_belgesi"+str(i)+".txt"
        my_source=path+filename
        my_dest=path+my_dest
        os.rename(my_source,my_dest)
        i+=1

if __name__ == '__main__':
        main()