'''
Split: # Dividir uma String (str)
Join: # Juntar uma lista (str)
Enumerate: # Enumerar elementos da lista (iteráveis)
'''''

# SPLIT
string = 'O Brasil é o o o país do futebol, o Brasil é penta.'
lista1 = string.split(' ')
lista2 = string.split(',')

for valor in lista1:
    print(valor)
    print(f'A palavra {valor} apareceu {lista1.count(valor)} vezes.') # Conta quantas vezes apareceu na lista.
print()
palavra = ''
contagem = 0
for valor in lista1:
    qntd_vezes = lista1.count(valor)
    if qntd_vezes > contagem:
        contagem = qntd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é {palavra} ({contagem} vezes).')
print()
for valor in lista2:
    print(valor.strip().capitalize())

# JOIN
string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(lista)
print(string2)

# ENUMERATE
lista = ['Jõao', 'Maria', 'Arthur']

for indice, nome in enumerate(lista):
    print(indice, nome)

n1, n2, n3 = lista
print(n3)