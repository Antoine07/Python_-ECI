from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


"""
render_template permet de prendre un fichier html et de l'afficher (moteur de template)
ce n'est la même chose que de renvoyer une chaine de caractères
"""
@app.route("/")
def home():
    return render_template('index.html')