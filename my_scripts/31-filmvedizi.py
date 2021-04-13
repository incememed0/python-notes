# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################

import requests

class theMovieDb:
    def __init__(self):
        self.url="https://api.themoviedb.org/3/"
        self.api_key="4c7f4d4698*********8576fef9"
    def getPopulars(self):
        response=requests.get(self.url+"movie/popular?api_key="+self.api_key+"&language=en-US&page=1")
        return response.json()
    def getsearchResult(self,keyword):
        response=requests.get(self.url+"search/keyword?api_key="+self.api_key+"&query="+keyword+"&language=en-US&page=1")
        return response.json()

movieApi=theMovieDb()
while True:
    secim=input("1- popular movies\n2- search movies\n3- create repository\n4- exit\nseçiminiz: ")
    if secim=="4":
        print("goodby!")
        break
    else:
        if secim=="1":
            movies=movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['original_title'])

        elif secim=="2":
            keyword=input("keyword: ")
            movies=movieApi.getsearchResult(keyword)
            for movie in movies['results']:
                print(movie['name'])
        elif secim=="3":
            pass
        else:
            print("hatalı seçim yaptınız.")
