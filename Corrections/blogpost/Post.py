from Config import app,db 

def create_posts():
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
    posts = Post.query.all()
    countPosts = len( posts )
    print(f"already created with posts ...NB posts {countPosts}")

    # si la table est créée mais qu'il n'y a pas de posts il faut créer donc on lance une exception pour la capturer et créer les posts
    if  len( posts ) == 0 :
        create_posts()

except:
    db.create_all() # la méthode de l'ORM pour créer toutes les tables
    create_posts()





