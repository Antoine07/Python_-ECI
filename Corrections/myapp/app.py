from flask import Flask, render_template

# import directement depuis l'espace de nom data la liste users
#from data import users

# import dans l'espace de nom du fichier Data.users la liste users 
from Data.users import users
# on fait un alias pour éviter la collision des noms des fonctions et des variables ( voir plus bas avec le nom de la fonction authors)
from Data.authors import authors as authors_data

# print(users)
# print(authors_data)

app = Flask(__name__)

# Exemple de route
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

"""
render_template permet de prendre un fichier html et de l'afficher (moteur de template)
ce n'est la même chose que de renvoyer une chaine de caractères
"""
@app.route("/")
def home():
    return render_template('index.html', users=users)

"""
Route pour afficher les auteurs : authors
"""
@app.route("/authors")
def authors():
    return render_template('authors.html', authors=authors_data)


"""
Route dynamique testez une route dynamique pour afficher une valeur dans la page Web
""" 
@app.route("/user/<id>")
def showUser(id):
    id = int(id) 
    user = None

    # On regarde si l'indice est un indice de la liste sinon par défaut user = None ( pas d'utilisateur )
    if 0 <= id < len(users):
        user = users[id]

    # print(user)

    return render_template('user.html', user = user)