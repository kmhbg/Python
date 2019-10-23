from pandas import DataFrame
import pandas as pd
from getpass import getpass
from passlib.hash import pbkdf2_sha256

database = "d:/python/users.csv"
readCsv = pd.read_csv(database)

class User:
    def __init__(self,username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def greeting(self):
        return ("Welcome %s, you are now loggedin"%(self.username))

def menu():
    print(""" 
        Welcome!
        Make a choice below
        1.  Sign in
        2. 
    
    """)

def hashPassword(password):
    hash = pbkdf2_sha256.hash(password, rounds=20000, salt_size=16)
    return hash
    
def deHashPassword(password, hash):
    return pbkdf2_sha256.verify(password, hash)




def login():
    loginCount = 0
    for retry in range(3):
        u = input("Enter username: ")
        p = getpass()
        tryLogin = getIndex(u, p)
        if tryLogin == True and loginCount <= 3:
           
            break
        
        elif loginCount <= 3:
            loginCount = loginCount + 1
            print("Login failed, try again you have %s times left"%(3-loginCount))
        
    else:
        print("You are done!")

def createUser():
    """Creates a new user to a CSV database and are using
        function "checkDatabase" if the entry exists"""
    username = checkDatabase("username", "username")
    password = input("Enter desired password: ")
    email = checkDatabase("email", "emailadress")
    newUser = User(username, hashPassword(password), email)
    data = {"username": [newUser.username],"password": [newUser.password], "email":[newUser.email]}
    df = DataFrame(data, columns=["username", "password", "email"])
    df.to_csv(r"d:/python/users.csv", index = None, header=False, mode="a")
    

def checkDatabase(column, typeOfEntry):
    """Checking the database for if the desired entry exist"""
    data = input("Enter desired %s: "%(typeOfEntry))
    for user in readCsv[column]:
        while True:    
            if user == data:
                print("Username is already taken, choose another one.")
                data = input("Enter desired %s: "%(typeOfEntry))
            else:
                break
    return data

                
   
def getIndex(user, password):
    while True:
        for u in readCsv["username"]:
        
            if u == user:
                get = readCsv.index[readCsv["username"] == user].tolist()

                if deHashPassword(password, readCsv.iat[get[0],1]) == True:
                    print("logged in")
                    return True
                    
                else:
                    print("Error wrong user or password")
                    return False

    
"""  def getIndex(user, password):
    while True:
        for u in readCsv["username"]:
        
            if u == user:
                get = readCsv.index[readCsv["username"] == user].tolist()

                if password == readCsv.iat[get[0],1]:
                    print("logged in")
                    return True
                    
                else:
                    print("Error wrong user or password")
                    return False

      """  



def readDatabase():
    result = pd.read_csv(database)
    return result

menu()
#getIndex("test","1")
#login()
#hashPassword("test")
#createUser()