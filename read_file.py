#count to lines in  a file 

fhand= open('Data_J&J.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line count: ', count)