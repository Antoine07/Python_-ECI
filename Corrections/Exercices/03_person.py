persons = { (1, 2, 3) : ["Alan", "Albert" ], (3,5,7) : ["Sophie"] }

# méthode impérative 
s = 0
for  person in persons:
    print(persons[person])
    s += sum( person )

print(s)

# approche pythonique de la programmation déclaratif 
print(  sum( sum(p) for p in persons )  )