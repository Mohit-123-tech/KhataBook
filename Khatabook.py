import sqlite3
from colorama import Fore
import json
import datetime as DT
from os import system
import playsound as ps


Menu = """
    SELECT OPTION
Create New Khata [1]
Add To khata [2]
Show Khata [3]
Delete Khata [4]
Exit [0]
"""

system("clear")
print(Fore.GREEN,Menu,Fore.WHITE)

API = json.load(open("src/Json/api.json"))
Date = DT.date.today()
ps.playsound(API["StartupSound"])

class DataBase:
    def Createkhata(Name, Number):
        Connection = sqlite3.connect(API["DatabasePath"])
        Connect = Connection.cursor()

        Connect.execute(f"CREATE TABLE {Name+'_'+Number}(Number text,Date text,Amount text)")

        Connection.commit()
        Connection.close()


    def AddDataToKhata(Name, Number, Amount):
        Connection = sqlite3.connect(API["DatabasePath"])
        Connect = Connection.cursor()

        try:
            Connect.execute(f"INSERT INTO {Name+'_'+Number}(Number, Date, Amount) VALUES(?,?,?)", (Number, Date, Amount))
        except(Exception):
            print(Fore.RED,"USER NOT FOUND...?", Fore.WHITE)

        Connection.commit()
        Connection.close()


    def ShowData(Name, Number):
        Connection = sqlite3.connect(API["DatabasePath"])
        Connect = Connection.cursor()

        try :
            Connect.execute(f"SELECT * FROM {Name+'_'+Number}")
            return Connect.fetchall()

        except(Exception):
            pass
        
        Connection.commit()
        Connection.close()

    def DeleteKhata(Name, Number):
        Connection = sqlite3.connect(API["DatabasePath"])
        Connect = Connection.cursor()

        try:
            Connect.execute(f"DROP TABLE {Name+'_'+Number}")
            print(Fore.RED, "khata Deleted", Fore.WHITE)
        except(Exception) as e:
            print(e)

        Connection.commit()
        Connection.close()
