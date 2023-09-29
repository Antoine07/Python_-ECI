from flask import render_template
from Post import  Post
# Configuration de votre application
from Config import app, db 

@app.route("/")
def home():
    # ORM SQLAlchemy on demande tous les posts dans la table post de la base de données
    # en passant par l'ORM
    posts = db.session.query(Post).all()

    print(len( posts) )

    return render_template('posts.html', posts = posts)