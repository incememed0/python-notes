# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################

import requests

class Github:
    def __init__(self):
        self.api_url="https://api.github.com"
        self.token="ghp_E90*****************2FwJAH"

    def getUser(self,username):
        response=requests.get(self.api_url+"/users/"+username)
        return response.json()
    def getRepo(self,username):
        response=requests.get(self.api_url,"/users/"+username+"/repos")
        return response.json()
    def createRepo(self,name):
        response=requests.post(self.api_url+'/user/repos?access_token='+self.token,json={
            'name': name,
            'description': 'this is your fist repository',
            'homepage':'https://github.com',
            'private': True,
            'has_issues':True,
            'has_projects':True,
            'has_wiki':True
        })
        return response.json()

github=Github()

while True:
    secim=input("1- find user\n2- get repositor\n3- create repository\n4- exit\n seçiminiz: ")
    if secim=="4":
        print("goodby!")
        break
    else:
        if secim=="1":
            username=input("username: ")
            result=github.getUser(username)
            print(f"name: {result['name']}, public repos: {result['public_repos']}, follower: {result['followers']}")
        elif secim=="2":
            username=input("username: ")
            result=github.getRepo(username)
            for repo in result:
                print(repo["name"])
        elif secim=="3":
            name=input("repository name: ")
            result=github.createRepo(name)
            print(result)
        else:
            print("hatalı seçim yaptınız.")