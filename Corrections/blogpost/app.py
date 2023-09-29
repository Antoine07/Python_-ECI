from flask import Flask, render_template
from Post import  db, Post, app 
from flask_sqlalchemy import SQLAlchemy

@app.route("/")
def home():
    # ORM SQLAlchemy on demande tous les posts dans la table post de la base de données
    # en passant par l'ORM
    posts = db.session.query(Post).all()

    print(len( posts) )

    return render_template('posts.html', posts = posts)