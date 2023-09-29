from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

# création de l'application une seule fois
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
app.app_context().push()

db = SQLAlchemy(app)