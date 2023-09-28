from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBas

class Post(DeclarativeBase):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

db = SQLAlchemy(model_class=Post)

db.create_all()

users = [
    {"id": 1, "title": "First Post", "content": "Content of the first post"},
    {"id": 2, "title": "Second Post", "content": "Content of the second post"},
    {"id": 3, "title": "Third Post", "content": "Content of the third post"},
    # Add more posts as needed
]

for p in posts :
    newP= Post(id = p['id'], title = p['title'] , content = p['content'])
    db.session.add(newP)

db.session.commit()