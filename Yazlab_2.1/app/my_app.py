from flask import Flask
from .controllers import MySessionInterface
from .views import home,users

def create_app():    
    app =Flask(__name__, template_folder="templates",static_folder="static")
    app.config.from_pyfile("config.py")
    app.secret_key="b?039eruıf3__"
    app.config["VERSİON"]="1.0.0"
    app.session_interface=MySessionInterface()

    if app.config["VERSİON"]=="1.0.1":
        pass
    elif app.config["VERSİON"]=="1.0.2" :
        pass

    app.register_blueprint(home.bp)
    app.register_blueprint(users.bp)

    return app
 