import sqlite3
import os
import datetime


currentdirectory=os.path.dirname(os.path.abspath(__file__))
def User_sorgu(username,password):
    sqlconnection=sqlite3.Connection(currentdirectory+"\db.db")
    cursor=sqlconnection.cursor()
    statement=f"SELECT * from Users where name='{username}' AND password='{password}';"
    cursor.execute(statement)
    rows=cursor.execute(statement)
    
    rows=rows.fetchall()
    sqlconnection.commit()
    sqlconnection.close()
    
    if len(rows)==1:
        print("buldu")
        #loginTime = datetime.datetime.now()
        giris(username)
        return True 
    else:
        return False



def GirisTarih(username):
    sqlconnection=sqlite3.Connection(currentdirectory+"\db.db")
    cursor=sqlconnection.cursor()
    statement=f"SELECT loginTime from Users where name='{username}' ;"
    cursor.execute(statement)
    rows=cursor.execute(statement)
    
    rows=rows.fetchall()
    sqlconnection.commit()
    sqlconnection.close()
    
   
    return rows


def Arac_sorgu(username):
    sqlconnection=sqlite3.Connection(currentdirectory+"\db.db")
    cursor=sqlconnection.cursor()
    statement=f"SELECT arac from vehicles where sahibi='{username}';"
    cursor.execute(statement)
    rows=cursor.execute(statement)
    rows=rows.fetchall()
    
    
    sqlconnection.commit()
    sqlconnection.close()

    return rows


def LoginTime_sorgu(username):
    sqlconnection=sqlite3.Connection(currentdirectory+"\db.db")
    cursor=sqlconnection.cursor()
    statement=f"Select loginTime from Users where name='{username}';"
    cursor.execute(statement)
    rows=cursor.execute(statement)
    rows=rows.fetchall()
    
    
    sqlconnection.commit()
    sqlconnection.close()
    
    return rows

def giris(username):
    updateTime = datetime.datetime.now()
    sqlconnection=sqlite3.Connection(currentdirectory+"\db.db")
    cursor=sqlconnection.cursor()
    statement=f"Update Users set loginTime='{updateTime}' WHERE Users.name='{username}'"
    cursor.execute(statement)
    sqlconnection.commit()
    sqlconnection.close()
    



def cikis(username):
    updateTime = datetime.datetime.now()
    sqlconnection=sqlite3.Connection(currentdirectory+"\db.db")
    cursor=sqlconnection.cursor()
    statement=f"Update Users set logoutTime='{updateTime}' WHERE Users.name='{username}'"
    cursor.execute(statement)
    sqlconnection.commit()
    sqlconnection.close()
    
    
