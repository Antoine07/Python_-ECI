
message = 'mississippi'

letters = set(message)

print( message.count( 'i') )

# première correction
stat = { }

for letter in letters:
    stat[letter] = message.count(letter)

print(stat)

# deuxième correction compréhension de liste
stat = { l: message.count(l) for l in letters }

print(stat)
