from flask import session
from app.models.models import User_sorgu,Arac_sorgu

def UserLogin(username,password):
    if User_sorgu(username, password):
        session["username"] = username
        return True
    else:
        return False



def UserLogout():
    if 'username' in session:
        del session["username"]
        return True
    else:
        return False

def GetCurrentUsername():
    username = ""
    loginAuth = False
    if "username" in session:
        username = session["username"]
        loginAuth = True
    return username, loginAuth
