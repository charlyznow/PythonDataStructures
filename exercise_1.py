print('Excercice extract word in position and change to string to float')
str = 'X-DSPAM-Confidence: 0.8475'
ipos = str.find(':')
print(ipos)
x = str[ipos+1:]  #Se usa el +1 para quitar el espacio desues de los : o se podria usar +2 para que borre eñ espacio en blanco

print(x)
#conversion de string a float
value = float(x)  
print(value)
print(value+42.0)

