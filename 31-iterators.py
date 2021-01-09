# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# iterators:
liste=[1,2,3,4]
degisken=iter(liste)
#print(next(degisken))
#print(next(degisken))
#print(next(degisken))
#print(next(degisken))
# print(next(degisken)) # StopIteration hatası verir, devam edicek eleman yok
for i in liste:
    print(i)
#######################
print("-------------")
#######################
while True:
    try:
        eleman=next(degisken)
        print(eleman)
    except StopIteration:
        break
####################################
class Mynumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=self.stop:
            x=self.start
            self.start+=1
            return x
        else:
            raise StopIteration
liste=Mynumbers(10,20)
myiter=iter(liste)
print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in liste:
    print(x)
