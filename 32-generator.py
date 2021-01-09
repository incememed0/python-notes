# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
# generator: bellekte yer işgal etmeyen bir iterator üretiyor
########
def cube():
    result=[] # liste bellekte yer kaplamakta
    for i in range(5): # hedefimiz bellekte gereksiz yer kaplamasını önlemek
        result.append(i**3)
    return result
print(cube())
####
def generatorcube():
    for i in range(5):
        yield i**3  # yield: bir değer üretiyor ve bu degeri bana gönderiyor, gönderdikten
        # sonra bu değer bir yerde saklanmıyor. bu değere ulaşmak istediğim zaman bi daha ulaşamam
print(generatorcube()) # bize tahsis edilen yer çıktısı verilir
for i in generatorcube():
    print(i)

print("-------------------------")
liste=[i**3 for i in range(5)] # düz hali
print(liste)
liste=(i**3 for i in range(5)) # generator
print(liste)
for i in liste:
    print(i)
