
# object 
def gen():
    for i in range(0, 10):
        # cursor à chaque itération il avance et après il s'arrête en lançant une exception
        yield i

print(gen())
print(list ( gen() ) )

g = gen()
print( next ( g ) )
print( next ( g ) )
print( next ( g ) )
print( next ( g ) )
print( next ( g ) )
print( next ( g ) )
print( next ( g ) )
print( next ( g ) )
print( next ( g ) )
print( next ( g ) )
# print( next ( g ) )