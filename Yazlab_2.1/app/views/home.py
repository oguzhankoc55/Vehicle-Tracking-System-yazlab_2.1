from operator import length_hint
from flask import render_template,Blueprint, request,abort
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from app.models.models import Arac_sorgu,GirisTarih
import pandas as pd
from app.controllers import GetCurrentUsername
import sys
sys.path.append("../")


global cred 
global app
global request1
data_10 = []
data_25 = []
data_34 = []
data_37 = []

def build():
    
    if not firebase_admin._apps:
        cred = credentials.Certificate("app./key.json") 
        app = firebase_admin.initialize_app(cred)

    
    request1 = firestore.client()
    data_25_docu = request1.collection(u'ALLCARS').document(str(25))
    data_25_doc = data_25_docu.get()._data
    data_10_docu = request1.collection(u'ALLCARS').document(str(10))
    data_10_doc = data_10_docu.get()._data
    data_34_docu = request1.collection(u'ALLCARS').document(str(34))
    data_34_doc = data_34_docu.get()._data
    data_37_docu = request1.collection(u'ALLCARS').document(str(37))
    data_37_doc = data_37_docu.get()._data

    
    x_list10=[]
    y_list10=[]
    date_list10=[]
    time_point10=[]
    doc = data_10_doc

    for value, date in doc.items():
        x_list10.append(doc[value]['x'])
        y_list10.append(doc[value]['y'])
        date_list10.append(value)
        time = value.split(" ")
        saat = time[1]
        saat_birim = saat.split(":")
        toplam = (int(saat_birim[0])*60)+(int(saat_birim[1]))
        time_point10.append(toplam)
    
    for i in range(len(x_list10)):
        veri = {
        "x": 0,
        "y": 0,
        "date": 0,
        "time_p":0
        }
        veri.update({"x": x_list10[i]})
        veri.update({"y": y_list10[i]})
        veri.update({"date": date_list10[i]})
        veri.update({"time_p": time_point10[i]})
        data_10.append(veri)

    x_list25=[]
    y_list25=[]
    date_list25=[]
    time_point25=[]
    doc = data_25_doc

    for value, date in doc.items():
        x_list25.append(doc[value]['x'])
        y_list25.append(doc[value]['y'])
        date_list25.append(value)
        time = value.split(" ")
        saat = time[1]
        saat_birim = saat.split(":")
        toplam = (int(saat_birim[0])*60)+(int(saat_birim[1]))
        time_point25.append(toplam)
    
    for i in range(len(x_list25)):
        veri = {
        "x": 0,
        "y": 0,
        "date": 0,
        "time_p":0
        }
        veri.update({"x": x_list25[i]})
        veri.update({"y": y_list25[i]})
        veri.update({"date": date_list25[i]})
        veri.update({"time_p": time_point25[i]})
        data_25.append(veri)


    x_list34=[]
    y_list34=[]
    date_list34=[]
    time_point34=[]
    doc = data_34_doc

    for value, date in doc.items():
        x_list34.append(doc[value]['x'])
        y_list34.append(doc[value]['y'])
        date_list34.append(value)
        time = value.split(" ")
        saat = time[1]
        saat_birim = saat.split(":")
        toplam = (int(saat_birim[0])*60)+(int(saat_birim[1]))
        time_point34.append(toplam)
    
    for i in range(len(x_list34)):
        veri = {
        "x": 0,
        "y": 0,
        "date": 0,
        "time_p":0
        }
        veri.update({"x": x_list34[i]})
        veri.update({"y": y_list34[i]})
        veri.update({"date": date_list34[i]})
        veri.update({"time_p": time_point34[i]})
        data_34.append(veri)

    #data_37 = get_data(data_37_doc)

    
    x_list37=[]
    y_list37=[]
    date_list37=[]
    time_point37=[]
    doc = data_37_doc

    for value, date in doc.items():
        x_list37.append(doc[value]['x'])
        y_list37.append(doc[value]['y'])
        date_list37.append(value)
        time = value.split(" ")
        saat = time[1]
        saat_birim = saat.split(":")
        toplam = (int(saat_birim[0])*60)+(int(saat_birim[1]))
        time_point37.append(toplam)
    
    for i in range(len(x_list37)):
        veri = {
        "x": 0,
        "y": 0,
        "date": 0,
        "time_p":0
        }
        veri.update({"x": x_list37[i]})
        veri.update({"y": y_list37[i]})
        veri.update({"date": date_list37[i]})
        veri.update({"time_p": time_point37[i]})
        data_37.append(veri)






def arac_bul(arac_ismi):
    if arac_ismi == "10":
        return data_10
    if arac_ismi == "25":
        return data_25
    if arac_ismi == "34":
        return data_34
    if arac_ismi == "37":
        return data_37


def son_30_dk(time, isim):
    suanki_saat = time
    yarım_saat_oncesi = time-30 
    x_list=[]
    y_list=[]
    date_list=[]
    time_point=[]
    isim1=isim[0]
    if isim1 == "10":
        for veri in data_10:
            if veri["time_p"]>yarım_saat_oncesi and veri["time_p"]<suanki_saat:
                x_list.append(veri["x"])
                y_list.append(veri["y"])
                date_list.append(veri["date"])
    if isim1 == "25":
        for veri in data_25:
            if veri["time_p"]>yarım_saat_oncesi and veri["time_p"]<suanki_saat:
                x_list.append(veri["x"])
                y_list.append(veri["y"])
                date_list.append(veri["date"])
    if isim1 == "34":
        for veri in data_34:
            if veri["time_p"]>yarım_saat_oncesi and veri["time_p"]<suanki_saat:
                x_list.append(veri["x"])
                y_list.append(veri["y"])
                date_list.append(veri["date"])
    if isim1 == "37":
        for veri in data_37:
            if veri["time_p"]>yarım_saat_oncesi and veri["time_p"]<suanki_saat:
                x_list.append(veri["x"])
                y_list.append(veri["y"])
                date_list.append(veri["date"])

    
    
    data_new = []
    for i in range(len(x_list)):
        
        veri = {
        "x": 0,
        "y": 0,
        "date": 0
        }
        veri.update({"x": x_list[i]})
        veri.update({"y": y_list[i]})
        veri.update({"date": date_list[i]})
        data_new.append(veri)


    data_new = pd.DataFrame(data_new)
    data_new = data_new.sort_values("date",ignore_index=True)

    x_db = data_new["x"]
    y_db = data_new["y"]
    dt_db = data_new["date"]

    data_new2 = []
    for i in range(len(x_db)):
        veri = {
        "x": 0,
        "y": 0,
        "date": 0
        }
        veri.update({"x": x_db[i]})
        veri.update({"y": y_db[i]})
        veri.update({"date": dt_db[i]})
        data_new2.append(veri)   

    return data_new2    

def get_data_time(saat1,saat2,dakika1,dakika2,arac):


        data_aractime=[]
        
        if arac == "10":
            data_aractime=data_10
        if arac == "25":
            data_aractime=data_25
        if arac == "34":
            data_aractime=data_34
        if arac == "37":
            data_aractime=data_37
        

        
        
        x_listaractime=[]
        y_listaractime=[]
        date_listaractime=[]
        dgr_1 = (int(saat1)*60)+int(dakika1)
        dgr_2 = (int(saat2)*60)+int(dakika2)

        if dgr_2<=dgr_1 :
            return 0
        
        for veri in data_aractime:
            if veri["time_p"]>(dgr_1) and veri["time_p"]<(dgr_2):
                x_listaractime.append(veri["x"])
                y_listaractime.append(veri["y"])
                date_listaractime.append(veri["date"])
        

        
        
        data_yeni2 = []
        for i in range(len(x_listaractime)):
            veri = {
            "x": 0,
            "y": 0,
            "date": 0
            }
            veri.update({"x": x_listaractime[i]})
            veri.update({"y": y_listaractime[i]})
            veri.update({"date": date_listaractime[i]})
            data_yeni2.append(veri)

        data_yeni2 = pd.DataFrame(data_yeni2)
        data_yeni2 = data_yeni2.sort_values("date",ignore_index=True)

        x_db_2 = data_yeni2["x"]
        y_db_2 = data_yeni2["y"]
        dt_db_2 = data_yeni2["date"]
        data_new4 = []
        boyut = int(len(x_db_2))
        boyut = boyut-1
        for i in range(boyut):
            veri_ = {
                "x": 0,
                "y": 0,
                "date": 0
            }
            veri_.update({"x":x_db_2[i]})
            veri_.update({"y":y_db_2[i]})
            veri_.update({"date":dt_db_2[i]})
            data_new4.append(veri_)

        
        return data_new4

bp=Blueprint("home",__name__,template_folder="../templates",static_folder="../static")

@bp.route("/")
def Index():
    username, login_auth = GetCurrentUsername()
    
    return render_template("login.html", username=username, login_auth=login_auth)

@bp.route("/login")
def Login():
    username, login_auth = GetCurrentUsername()
    
    return render_template("login.html", username=username, login_auth=login_auth)
@bp.route("/map1")
def map1():
    username, login_auth = GetCurrentUsername()
    now = datetime.now()

    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string=dt_string.split(" ")[1]
    x1=dt_string.split(":")[0]
    x2=dt_string.split(":")[1]
    print("Saat:"+x1+"Dakika:"+x2)	
    
    Giris=GirisTarih(username)
    # x = str(datetime.datetime.now())
    # x=x.split(" ")[1]
    # x1=x.split(":")[0]
    # x2=x.split(":")[2].split(".")[0]
    # x=x1+":"+x2
    # x=x.split(":")
    
    suankisaat=(int(x1)*60 +int(x2))
    vehichles=Arac_sorgu(username)
    
    build()
    arac1 = vehichles[0]
    arac2 = vehichles[1]
    data_1= son_30_dk(suankisaat,arac1)
    
    data_2= son_30_dk(suankisaat,arac2)
    
    return render_template('map1.html',  data1 = data_1 ,data2 = data_2,Giris=Giris)
    

@bp.route("/secim")
def secim():
    
    username,login_auth = GetCurrentUsername()
    Giris=GirisTarih(username)
    vehichles=Arac_sorgu(username)
    varmi = {
            "10": 0,
            "25": 0,
            "34": 0,
            "37": 0
            }
    
    for vehichle in vehichles:
        if(vehichle[0]=='10'):
            {varmi.update({"10":1})}
        if(vehichle[0]=='25'):
            {varmi.update({"25":1})}
        if(vehichle[0]=='34'):
            {varmi.update({"34":1})}
        if(vehichle[0]=='37'):
            {varmi.update({"37":1})}      
    
    return render_template("secim.html",username=username,login_auth=login_auth,varmi=varmi
    ,Giris=GirisTarih(username))



@bp.route("/map2",methods=["GET","POST"])
def map2():
    username,login_auth = GetCurrentUsername()
    Giris=GirisTarih(username)     
    if request.method == "POST":
        if request.form:
            if "saat1" in request.form and "saat2" in request.form and "arac" in request.form:
                saat1 = request.form["saat1"]
                saat2 = request.form["saat2"]
                dakika1 = request.form["dakika1"]
                dakika2 = request.form["dakika2"]
                
                arac = request.form["arac"]
                print("arac"+arac)
                

                data= get_data_time(saat1,saat2,dakika1,dakika2,arac)
                if data==0:
                    return secim() 
                
                else:
                    return render_template('map2.html',  data = data )
                
                    
        abort(400)
    username, login_auth = GetCurrentUsername()
    return render_template("login.html", username=username, login_auth=login_auth,Giris=Giris)