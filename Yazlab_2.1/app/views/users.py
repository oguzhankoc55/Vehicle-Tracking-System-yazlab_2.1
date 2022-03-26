from flask import request, redirect, url_for, render_template, abort,Blueprint
from app.controllers import UserLogin, GetCurrentUsername, UserLogout 

import sqlite3
import os
from app.models.models import  cikis


currentdirectory=os.path.dirname(os.path.abspath(__file__))

bp=Blueprint("users",__name__,template_folder="../templates")

@bp.route("/",methods=["GET","POST"])
def Login():
    if request.method == "POST":
        if request.form:
            if "username" in request.form and "password" in request.form:
                username = request.form["username"]
                password = request.form["password"]
                if UserLogin(username, password):
                #if User_sorgu(username, password):
                    return redirect(url_for("home.map1"))#secim ekranı
                else:
                    return redirect(url_for("home.Login"))
                #SELECT name from Database
        abort(400)
    username, login_auth = GetCurrentUsername()
    return render_template("login.html", username=username, login_auth=login_auth)

@bp.route("/logout")
def Logout():
    username, login_auth = GetCurrentUsername()
    if UserLogout():
        cikis(username)
        return redirect(url_for("home.Index"))



