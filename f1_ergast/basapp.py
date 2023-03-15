import os
import shutil
import zipfile
import sqlite3
from datetime import datetime
import pysftp
import pandas as pd

db_file = "./database.db"
host_key = b"AAAAB3NzaC1yc2EAAAADAQABAAABAQCAbeYJ6B9xWFsPX0I445XZrfB1LZOQ9JTUYU9VLnSPddxFxoi+djaMVh7ErvpKc08ASwt5Np/2ElIYr0FKiDAX23Xez/5ZyiUhhTHJyp8Y6ev2FXgL7iN3nCcdh8boPYKD9C8d1B74GKgpwxa7fqMMyd/DtpuC+Una0PVhwoJQuLNzC2Di40fJftvmjIQHAfaDlrtGdIu3D87d15cOQ1hJhG+BO4kADhilS5BsxDEfIJW2gcfigCHQ0qd3tcU/0EztRk9eXqwq/zziehzJAN79J9p8+g1ikKMDwo6jKTqI7hKlpbauZ/5YDxMHTY3K4edLhWMmF4DKIY5T3j43C+nd"
host = "eumft.nielseniq.com"
remote_path = "FTMS_PRD_01_EU_RMS_DDE_FTMS_MELITTA_SCANDI_AB_SE_PULL_DDE_60685"
username = "FTMS_PRD_01_EU_33066"
password = "WM87%sncan"
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


def connect_sftp():
    with pysftp.Connection(host, username=username, password=password, cnopts=cnopts) as sftp:
        with sftp.cd():
            sftp.chdir(remote_path)
            if not sftp.listdir():
                return "Mappen är tom, ingen ny data från Nielsen!"
            else:
                for file in sftp.listdir():
                    if not check_file_in_db(file):
                        sftp.get(file)
                        save_zip(file)
                        return f"Filen {file} är nerladdad, Uppdatera Nielsen via genvägen på ditt skrivbord!"
                    else:
                        return "Inga nya filer sedan du uppdaterade sist!"


def create_db_table():
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute('''
          CREATE TABLE IF NOT EXISTS files
          (file_name TEXT,download_date DATE)
          ''')
    con.commit()


def insert_to_db(filname):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO files (file_name, download_date) VALUES ('{filname}','{datetime.today().strftime('%Y-%m-%d')}')")
    con.commit()


def check_file_in_db(filname):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    exists = cur.execute(
        f"select exists(select file_name from files where file_name = '{filname}')")
    con.commit()
    if cur.fetchone():
        return True

    else:
        return False


def read_database():
    con = sqlite3.connect("./database.db")
    df = pd.read_sql_query("SELECT * FROM files", con)
    return df


def save_zip(filename):
    create_db_table()
    path = "//se-he-mh-fs01/Helsingborg/ADMINISTRATION/IT/PROGRAM/NIelsen/Database"
    file_path = f"//se-he-mh-fs01/Helsingborg/ADMINISTRATION/IT/PROGRAM/NIelsen/{filename}"
    insert_to_db(filename)
    shutil.move(f"./{filename}", file_path)
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(path)


def run():
    connect_sftp()
    # print(read_database())


if __name__ == '__main__':
    run()
