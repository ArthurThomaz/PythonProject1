'''
Lambda - Funções Anônimas
'''''

a = lambda x, y : x * y
print(a(2, 2))

lista = [
    ['p1', 13],
    ['p2', 5],
    ['p3', 22],
    ['p4', 7],
    ['p5', 2],
]
lista.sort(key=lambda item: item[1])
print(lista)

print(sorted(lista, key=lambda i: i[1], reverse=True))
