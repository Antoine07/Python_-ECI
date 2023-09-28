# Introduction Python

Python est langage objet multi-paradigme. Il est doté d'un typage dynamique fort. C'est un langage libre. 
Ce langage peut s'adapter à tout type de contexte grâce à de nombreux modules (extensions). 
Il est très répendu dans le monde scientifique et notamment dans le calcul numérique. 
Ce langage a été conçu par Guido van Rossum (Pays-Bas). Le début de ce langage commence pendant des vacances de Noël où le concepteur 
décide de travailler à sa création, fan des Monty Python il décide de baptiser son langage Python. 
Le langage  utilise l'indentation comme syntaxe.

Pour toutes les règles de Python qu'il faut suivre vous pouvez importer dans la console le module this :

```python
import this
```

Une règle de Python que nous suivrons dans le cours par exemple c'est : "Il vaut mieux être explicite qu'implicte".

## Installation
![Installation]{https://www.python.org/downloads/
Installer également Ipython à l'aide de pip, équivalent de npm
Utilisez Visual Studio Code 
Dans VS installez les modules suivants : Python Extension Pack Don Jayamanne
Ainsi que Python ms-python-python 

## LEGB
Nous allons préciser tout de suite une notion fondamentale sur le mécanisme de portée de variable en Python.
										
- L pour localement, Python regarde si vous avez défini la variable localement.
- E pour englobante, Python regarde si la variable n'est pas définie dans la première fonction englobante puis remonte ...
- G pour globalement, Python va alors chercher la variable de manière globale.

- B pour Builtins, Python regarde alors dans le module Builtins.

## Exemple LEGB

```python

# Variables gloables
"""
Définition des variables dans le script

LEGB 
"""

# G espace global
a = 101
b = 22

def foo():
    b = 1
    # E englobant puis il remonte
    def baz():
        # Python b regarde localement L
        print(b)
        print(a)

    baz()

print( foo() )

# Dans cet espace d'autres variables définies elles peuvent bien sûr dans l'espace de ce script être re-définie
import builtins

# On écrase la définition de print chose à ne pas faire évidemment
print = 1
```

- Passage d'arguments à une fonction 

```python
def f(a, b):
	return a, b
# on peut appeler les arguments dans l'ordre que l'on souhaite
x, y = f(b = 1, a = 3)

# On peut utiliser un tuple pour passer des arguments
def g(*t):
	return t

g(1,2,3) # 1,2,3

# Ou en utilisant un passage par dictionnaire
def h(**t):
	return t

h(a =1, b= 2, c =3) # { 'a' : 1, 'b' : 2, 'c' : 3 }
```

## Quelques définitions de base

Python utilise l'indentation comme syntaxe.

- Définition d'une fonction

```python
def myFunction(a, b):
	print(a + b)
```

- Les condtions

```python
if True :
	print("Bonjour tout le monde")
else: 
	print("Aurevoir tout le monde")
```

Un exemple avec if elif (il else if)

```python
a = 5
if a > 5:
	a = a + 1
elif a == 5:
    a = a + 1000
else:
    a = a - 1
```

- Valeurs booleans :

```python
True
False
```

- La structure d'une boulce en Python

```python
 # Boucle de 1 à 9
for x in range(1, 10):
	print(x)

# Boucle de 0 à 9
for x in range(10):
	print(x)
```

- Boucle tant que

```python
count = 0
while True:
	count += 1
	if count > 100:
		break
```

## Introduction aux Structures de données en Python

En Python une grande force du langage c'est les structures de données. Elles permettent 
de manipuler les données avec beaucoup d'intelligence et d'optimisation. 
Python est un langage adapté au Big Data par exemple, notamment pour sa grande richesse au 
niveau des structures de données.

### Définition d'une liste

Une liste est une suite de valeurs séparées par une virgule et placées entre crochets : 

```python
l = [1,2,3,4,5]
l[0] # 1
l[-1] # 5

# Slicing
l[-2:]
```
### l'opérateur : sur les listes

```python
l = [1,2,3,4,5]

l[1:-1] # retourne [2,3,4]

l[:2] # retourne [1,2] s'arrête à l'indice 2

# l[start:end:step]
l[::2] # [1,3,5] début fin par pas de 2 
```
	
## Les listes et quelques méthodes

```python
l = []
l.append(10) # ajouter 10 à la liste

# Ajoute tous les éléments d'un itérables
l.extend( x*x for x in range(10))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# insérer un élément à une position donnée, ici indice 2 on insère 100
l.insert(2, 100)
# [0, 1, 100, 4, 9, 16, 25, 36, 49, 64, 81]

# pop retirer un élément à l'indice 2 
l.pop(2)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# pop retire le dernier élément de la liste
l.pop() 
# [0, 1, 4, 9, 16, 25, 36, 49, 64]

# renvoie l'indice du premier élément trouvé ici 2
l.index(4)

# compte le nombre d'élément 2 dans une liste
l.count(2)

# longueur de la liste
len(l)

# tri une liste par ordre croissant par référence
l.sort()

# ordre décroissant par référence
l.sort(reverse=True)

# Supprime tous les éléments d'une liste
l.clear()
```

Une liste n'est pas copiée elle a une même référence
Si vous copiez une liste dans une autre variable celle-ci sera référencée vers la même liste, elle n'est pas copiée.

```python
l = [1,2,3,4,5]
m =l
m[0] = 100
print(l, m) # [100, 2, 3, 4, 5] [100, 2, 3, 4, 5]
```

On notera également que les listes et les chaînes de caractères en Python ont des nombreuses propriétés en commun.

## Faire une shallow copy pour copier la liste

Il faut faire ce que l'on appelle une shallow copy pour copier une nouvelle liste dans une nouvelle variable.C'est une copie peu profonde.

```python
q = l[:]
```

Remarque sur la copie peu profonde (shallow copy)

```python
# il y a 4 références ici 
r = [[1, 2], [3, 4], [5, 6]]

# shallow copy ne fait la copie que de la première 
t = r[:]
t[0][0] = 100

print(r, t)
# [[100, 2], [3, 4], [5, 6]] [[100, 2], [3, 4], [5, 6]]
```


## Listes d'exercices


Pour parcourir une liste 

```python
users = [
    {
        "id": 0,
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30,
        "bio": "Développeur Python passionné. Amateur de jeux vidéo."
    },
    {
        "id": 1,
        "name": "Alice Smith",
        "email": "alice@example.com",
        "age": 28,
        "bio": "Ingénieure logiciel avec une expertise en Python. Aime la randonnée."
    },
]


for user in users:
    print(user['name'])

```

## 01 Exercice boucle

Paroucir et afficher les données à l'intérieur de liste de listes suivantes :

```python
r = [[1, 2], [3, 4], [5, 6]]
```

## 02 Exercice users

importez les users dans un fichier app.py et affichez clairement le nom et l'age de chaque user.