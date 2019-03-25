from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relationships.db'
db = SQLAlchemy(app)


class TaxiUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName= db.Column(db.String(30),nullable=False)
    lastName= db.Column(db.String(30), nullable=False)
    password= db.Column(db.String(30), nullable=False)
    conf_password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone_num = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(30), nullable=False)
    taxi_company = db.Column(db.String(30), nullable=False)
    def __init__(self,firstName,lastName,password,conf_password,email,phone_num,city,taxi_company):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.conf_password = conf_password
        self.email = email
        self.phone_num = phone_num
        self.city = city
        self.taxi_company = taxi_company
db.create_all()
db.session.commit()
