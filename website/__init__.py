from flask import Flask
import pymysql
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db=SQLAlchemy()
DB_NAME="database.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='sdfghgjbk sdfghj'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLAlCHEMY_TRACK_MODIFICATIONS']= False

    db.init_app(app)  

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User, Note
    # import models
    with app.app_context():
        db.create_all()
    #create_database(app)


    login_manager=LoginManager()
    login_manager.login_view='auth.login' #where to redirect if user is not logged in
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))



    return app

# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         with app.app_context():
#             db.create_all()
#         print('Database Created!')
