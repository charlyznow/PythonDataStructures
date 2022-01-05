"""fruit= 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index,letter)
    index  = index + 1


fruit = 'banana'
for letter in fruit:
    print(letter)




word = 'banana'
count= 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


for i in 'banana':
    print(i)


s = 'Monty Python'
index = 0
while index < len(s):
    letter = s[index]
    print(index, letter) 
    index = index + 1


print(s[0:4])

s = 'Monty Python'
print(s[6:7])

s = 'Monty Python'
print(s[6:20])

s = 'Monty Python'
print(s[:4])

s = 'Monty Python'
print(s[6:])

s = 'Monty Python'
print(s[:])


fruit = 'banana'
if 'a' in fruit:
    print("found it")

    
"""
word = 'bananas'

if word == 'banana':
     print('All right, bananas.')

if word < 'banana':
    print('Yoour word, ' + word + ' , comes before banana')
elif word > 'banana':
    print('Your word , ' + word + ' , comes after banana')
else:
    print('All right, bananas')