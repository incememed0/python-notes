# author: Ercan Atar
# linkedin.com/in/ercanatar/
################################################

import json
import os

class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedIn=False
        self.currentUser={}
        #load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("35-deneme.json"):
            with open("35-deneme.json","r",encoding="utf-8") as file:
                users=json.load(file)
                for user in users:
                    user=json.loads(user)
                    print(user["username"])
                    newUser=User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append((newUser))
            print(self.users)

    def register(self,user:User):
        self.users.append(user)
        self.saveToFile()
        print("kullanıcı oluşturuldu")

    def login(self,username,password):
        for user in self.users:
            if user.username==username and password==password:
                self.isLoggedIn=True
                self.currentUser=user
                print("login yapıldı.")
                break
    def logout(self):
        self.isLoggedIn=False
        self.currentUser={}
        print("çıkış yapıldı")

    def identity(self):
        if self.isLoggedIn:
            print(f"username: {self.currentUser.username}")
        else:
            print("giriş yapılmadı")

    def saveToFile(self):
        list=[]
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("35-deneme.json","w") as file:
            json.dump(list,file)

repository=UserRepository()

while True:
    print(" menü ".center(50,"*"))
    secim=int(input("1-register\n2-login\n3-logout\n4-identity\n5-çıkış\nseçiminiz: "))
    if secim==5:
        print("goodbye!")
        break
    else:
        if secim==1:
            username = input("username: ")
            password = input("password: ")
            email = input("e-mail: ")
            user=User(username,password,email)
            repository.register(user)
            #print(repository.users)
        elif secim==2:
            if repository.isLoggedIn:
                print("zaten login oldunuz.")
            else:
                username = input("username: ") # login
                password = input("password: ")
                repository.login(username,password)

        elif secim==3:
            repository.logout() # logout
        elif secim==4:
            repository.identity() # identity username
        else:
            print("hatalı seçim yaptınız.")
