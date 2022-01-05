

abc = "hola yo soy una cadena"
stuff = abc.split()  #divide por espacio en blanco
print(stuff)
print(len(stuff))
print(stuff[2])

for w in stuff:
    print(w)

line =  'a lot                  of space'
etc = line.split()
print(etc)

line = 'one;two;three'
etc2 = line.split()
print(line)
print(len(etc2))

thing = line.split(';')
print(thing)

print(len(thing))



text = 'From stephen.marquez@uct.ac.za Sat Jan 5 09:13:23 2008'
words = text.split()
search = words[1]
print(search)

arroba = text.split('@')
print(arroba[1])

"""
dom = arroba.split()
dominio = dom[0]
print(dominio)


.split(' ')[0])
"""

print(text.split('@')[-1].split(' ')[0])

print(text.split('@')[-1])

