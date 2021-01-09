# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################
# regular expression: arama sonucunda bir sonuç döndürür, bir filtreleme işleminde kullanılır.
# kullanıcıdan sadece sayı bilgisi(cep no) gibi bilgileri alırken string ifade girmesi önlemek için kullanılır
# arama işleminde kullanılır
#################################
import re

degisken="python kursu: python programlama rehberi | 1453 saat"

#result=re.findall("python",degisken) # Girilen söz dizisinde anahtar kelime arayabilirsin.
#result=len(result) # kaç adet "python" yazısı geçtiğini görebiliriz
#result=re.split(" ",degisken) # boşluk karakteri arıcaz, split metodu ise her boşlukta ifadeyi böler
##################
#result=re.sub(" ","-",degisken) # boşluk karakterlerine - ifadesini ekler
#result=re.search("ython",degisken) # anahtar kelimeyi söz dizisinde ilk bulduğu zaman döngü sona erer. span=(0,6) match='python'
#result=result.span() # konumunu burdan alabilirsin
#result=result.start() # kaçıncı karakterden başladığını gösteriyor
#result=result.end()
#result=result.group()
#result=result.string

#print(result)
#############################################################################
#############################################################################
"""
----------------------------------------------------------------------------------------------
[] - Köşeli parantezler arasına yazılan bütün karakterler aranır.
    [abc] => a  : 1 match
            ac  : 2 match
        python  : No matches
    
    [a-e]   =>  [abcde]
    [1-5]   =>  [12345]
    [0-39]  =>  [01239] 0,1,2,3,9 
    
    [^abc]  =>  abc dışındaki karakterler
    [^0-9]  =>  rakam olmayan karakterler
"""
#result=re.findall("[abc]",degisken)
#print(result)
"""
----------------------------------------------------------------------------------------------
. - Herhangi bir karakteri belirtir.
    ..  =>  a   : No match
            ab  : 1 match
           abc  : 1 match
          abcd  : 2 matches

"""
#result=re.findall("...",degisken) # 3lü gruplar halinde yazar.
#result=re.findall("py..on",degisken) #
#print(result)
"""
-----------------------------------------------------------------------------------------------
^ - Belirtilen karakterlerle başlıyor mu?
    ^a  =>  a   : 1 match
           abc  : 1 match
           bac  : No match
"""
result=re.findall("^p",degisken)
print(result)