from . import db
# from flask_login import UserMixin
# from sqlalchemy.sql import func

# class User(db.Model,UserMixin):
#     id=db.Column(db.Integer,Primary_key=True)
#     email=db.Column(db.String(150), unique=True)
#     password=db.Column(db.String(150))
#     first_name=db.Column(db.String(150))


# class Note(db.Model):
#     id=db.Column(db.Integer,Primary_key=True)
#     data=db.Column(db.String(10000))
#     data=db.Column(db.DateTime(timezone=True, default=func.now()))