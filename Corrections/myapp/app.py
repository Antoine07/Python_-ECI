from flask import Flask, render_template

# import directement depuis l'espace de nom data la liste users
#from data import users

# import dans l'espace de nom du fichier Data.users la liste users 
from Data.users import users

print(users)


app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


"""
render_template permet de prendre un fichier html et de l'afficher (moteur de template)
ce n'est la même chose que de renvoyer une chaine de caractères
"""
@app.route("/example")
def example():
    return render_template('index.html', data=[{"a" : 1}, { "a" : 2}])