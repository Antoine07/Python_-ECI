# SQLAlchemy

## Installation Windows

récupérez les sources de SQLlite : https://www.sqlite.org/download.html

sqlite-dll-win64-x64-xxxxxxx.zip

Ajoutez dans les variables d'environnement le chemin vers 

Lancez votre terminale et testez si SQLite est disponible 

```bash
sqlite3 --version
```

## Installation Mac

Si ce n'est pas déjà installée sur votre machine, vérifiez avant dans un terminale :

```bash
sqlite3 --version
```

Vous pouvez le faire avec brew https://brew.sh/

Puis :

```bash
brew install sqlite
```

## Mise en place de SQLAlchemy pour un projet Flask

Installez les dépendances suivantes ORM ( Object Relation Model ), il permet de se connecter à la base de données en mappant les données dans des objets ( des classes en Python ).

Pour schématiser vous avez : un table en DB et un objet en Python qui permet de lier les deux deux.

```txt

table post <-> Post une class

```

### Installation

```bash
pip install Flask-SQLAlchemy
```

- Créez un projet blogpost sous Mac

Pensez à désactiver l'ancien environnement 

```bash
deactivate
```

Puis dans le bash activer votre nouvel environnement, par principe on met un point devant le dossier de configuration ou d'environnement. 


```bash
python -m venv .blogpost

# activate env .blogpost
. .blogpost/bin/activate
```

### Création de la base SQLite de données dans le projet 

à la racine du projet créez le fichier **post.db** base de données sqlite


- Créez le fichier Post.py modèle pour la création de la table post ( c'est une option ) et surtout le Mapping des données.

Lorsque l'on crée un table SQL nécessairement on doit créer un identifiant unique PK (primary key) pour identifier de manière univoque une ligne de la table. 

```python
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

# l'application Flask blogpost
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

# l'application Flask blogpost
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
app.app_context().push()

db = SQLAlchemy(app)

# ORM <=> connexion à la base de données
class Post(db.Model):
    # une ligne doit avoir un identifiant unique, automatiquement incrémentée
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=True)

    # le constructeur est appelé lorsqu'on crée un objet
    def __init__(self, title, content):
        self.title = title
        self.content = content

# On doit créer la table si elle n'existe 

try:
    # on requete en demandant tous les posts de la table post
    Post.query.all()
    print("already created with posts ...")
# except tout seul capture tout type d'exception ( arret du programme )
except:
    db.create_all() # la méthode de l'ORM pour créer toutes les tables
    posts = [
                {"id": 1, "title": "First Post", "content": "Content of the first post"},
                {"id": 2, "title": "Second Post", "content": "Content of the second post"},
                {"id": 3, "title": "Third Post", "content": "Content of the third post"},
            ]

    for p in posts:
        newP = Post(title = p['title'], content = p['content'] )
        # on l'ajoute à la staging sans le commit ( pas encore effecivement créer )
        db.session.add(newP)
    
    db.session.commit()


```