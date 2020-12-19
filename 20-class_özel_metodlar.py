# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
#
class Film():
    def __init__(self,filmadi,yonetmen,sure):
        self.filmadi=filmadi
        self.yonetmen=yonetmen
        self.sure=sure
        print("init metodu")
    def __str__(self):
        return "string ifadesi kullanıldı" # kelime çıktısı veriyorsun
    def __len__(self):
        return self.sure # bu ifadenin kullanımında sayı kullanmalısın
    def __del__(self):
        print("ifade silindi")

f=Film("ahlat ağacı","nuri bilge ceylan",180)
print(str(f))
print(len(f))
del f # komutu yazmasam bile program kapatılırken zaten siliniyor