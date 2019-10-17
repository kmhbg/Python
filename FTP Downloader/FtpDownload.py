# Application for downloading latest data from a FTP server



import os 
import ftplib
import zipfile
import socket
import time
import datetime as dt
import configparser


def Main():

    # Makes a start config.ini file with standard values
    def makeConfigFile():
        config = configparser.ConfigParser()
        config["DEFAULT"] = {"serverAdress": "ftp.test.com", "userName": "User", "password": "Password", "databasePath": "My local path"}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    if os.path.isfile("config.ini"):
        print("Config already exist, using existing values!")
    else:
        print("Creating new configfile with standard values...")
        makeConfigFile()


    config = configparser.ConfigParser()
    config.sections()
    config.read("config.ini")



    
    serverAdress = config["DEFAULT"]["serverAdress"]
    userName = config["DEFAULT"]["userName"]
    password = config["DEFAULT"]["password"]
    databasePath = config["DEFAULT"]["databasePath"]
    files = []

    ftp = ftplib.FTP(serverAdress)
    ftp.login(userName, password)
    ftp.cwd("/")

    # Check the FTP for the latest file uploaded
    def getNewestFile(ftp, limit=None):
        for fileName in ftp.nlst():
            response = ftp.sendcmd("MDTM {}".format(fileName))
            _, mtime = response.split()
            files.append((mtime, fileName))

        for index, decorated_filename in enumerate(sorted(files, reverse = True)):
            if limit is not None and index >= limit:
                break

            _, filename = decorated_filename
            yield filename

    downloaded = []
    for filename in getNewestFile(ftp, limit=1):
        print ('Downloading ' + filename)

        with open(filename, 'wb') as file:
            ftp.retrbinary('RETR '+ filename, file.write)

        downloaded.append(filename)


    ftp.quit()

    with zipfile.ZipFile(downloaded[0],"r") as zip_ref:
        zip_ref.extractall(databasePath)

    print("File downloaded!")

if __name__ == "__main__":
  Main().makeConfigFile()
