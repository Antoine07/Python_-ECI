from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

app.app_context().push()

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=True)

    def __init__(self,  title, content):
        self.title = title
        self.content = content

    @staticmethod
    def create_database():
        return db.create_all()
