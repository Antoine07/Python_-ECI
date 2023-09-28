r = [[1, 2], [3, 4, 8], [5, 6]]

# on fait deux boucles car deux listes 
for vector in r :
    for v in vector:
        # le print ne fait de retour à la ligne deuxième argument
        print( f"vector : {v}", "") 
    print()