from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relationships.db'
db = SQLAlchemy(app)

class Example (db.Model):
    __tablename__ = 'example'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data',db.Unicode)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(20))
