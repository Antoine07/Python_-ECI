
number = -6523

# on a le signe
sign = "-" if number < 0 else "" 

# on retire le signe pour inverser la chaine ( le signe sera mis au début après )
number = abs(number)

# print ( len( str(number)  ) )
lenNumber = len( str(number)  )
chNumber = str(number)

s = ''

# start, end, step 
for i in range(0, lenNumber):
    # print(lenNumber - 1 - i)
    # print(chNumber[ lenNumber - 1 - i ])
    # On parcourt la chaine à l'envers
    s += chNumber[lenNumber - 1 - i ]

print(s)

s = sign + s 

print(int(s) )
