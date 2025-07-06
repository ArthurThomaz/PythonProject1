'''
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''''

#        0 1 2 3 4 5 6 7 8 9     - Positivo
lista = [1,2,3,4,5,6,7,8,9,10]
#   -   10 9 8 7 6 5 4 3 2 1     - Negativo

string = '1,2,3,4,5,6,7,8,9,10'

print(string[0])
print(lista[0])

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)

l1.append('A')
print(l1)

del(l1[0])
print(l1)

