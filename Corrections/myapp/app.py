from flask import Flask, render_template, request, redirect, url_for, flash

# import directement depuis l'espace de nom data la liste users
#from data import users

# import dans l'espace de nom du fichier Data.users la liste users 
from Data.users import users
# on fait un alias pour éviter la collision des noms des fonctions et des variables ( voir plus bas avec le nom de la fonction authors)
from Data.authors import authors as authors_data

# Variable de configuration
from flask.config import Config

# print(users)
# print(authors_data)


def is_user_exist(email, users):
    for user in users :
        # est ce que est présent dans le dictionnaire utiliser .values pour tester sur les valeurs et pas les clés 
        if email in user.values() :
            return True
    
    # on l'a jamais trouvé donc on retourne faux 
    return False

app = Flask(__name__)
app.config.from_pyfile('config.py')

print(app.config)

# Exemple de route
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

"""
render_template permet de prendre un fichier html et de l'afficher (moteur de template)
ce n'est la même chose que de renvoyer une chaine de caractères
vous pouvez donner deux noms à votre route 
"""
@app.route("/home")
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

@app.route("/author/<author_id>")
def showAuthor(author_id):
    id = int(author_id) 
    author = None 

    if 0 <= id < len(authors_data):
        author = authors_data[id]

    return render_template('author.html', author = author )


# Une méthode  get post (verbs HTTP) pour respectivement afficher et créer un user
@app.route('/add', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        email = request.form.get('email')
        # on vérifie que l'utilisateur n'existe pas déjà dans la liste users
        if is_user_exist(email, users):
            # la fonction prend deux paramètres le premier c'est le message et le deuxième c'est la catégorie du message ici error
            flash('user already exist', 'danger')

            return render_template('admin/add.html')
        
        # remarque request.form récupère toutes les valeurs du formulaire 
        users.append(request.form)

        flash( f'success add user {request.form.get("name")}', 'success')

        return redirect(url_for('home'))
        
    else:
        return render_template('admin/add.html')
