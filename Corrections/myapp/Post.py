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

# Post.create_database()

posts = [
            {"id": 1, "title": "First Post", "content": "Content of the first post"},
            {"id": 2, "title": "Second Post", "content": "Content of the second post"},
            {"id": 3, "title": "Third Post", "content": "Content of the third post"},
            # Add more posts as needed
        ]

for p in posts :
    newP= Post( title = p['title'] , content = p['content'])
    print(newP)
    db.session.add(newP)
db.session.commit()