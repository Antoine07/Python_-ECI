from Data.users import users 

print("----------")

"""
Les try / except permettent de gérer les exceptions qui arrêtent les scripts, avec un try/except on capture l'exception et le script continu

"""

for user in users :
    age = None # valeur Python qui veut dire pas valeur (neutre)
    name = user['name']
    try:
        age = user['age']
    except KeyError:
        age = "pas d'information"

    print(f"Name : {name}, age : { age }")

print("----------")




