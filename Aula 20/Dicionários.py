d1 = {'chave1': 'valor da chave.'}
d1['nova_chave'] = 'Valor da chave2.'
print(d1['chave1'])


clientes = {
    'cliente1' : {
        'nome': 'Arthur',
        'sobrenome': 'Thomaz',
    },
    'cliente2' : {
        'nome': 'Isabella',
        'sobrenome': 'Borges',
    },
    'cliente3': {
        'nome': 'Christiane',
        'sobrenome': 'Teixeira',
    },
    'cliente4': {
        'nome': 'Pedro',
        'sobrenome': 'Alves',
    },
}
for clientes_k, clientes_v in clientes.items():
    print(f'{clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

import copy
d1 = {1: 'a', 2: 'b', 3: 'Arthur', 8: ('Jabuti', 'Feijão')}
v = copy.deepcopy(d1)
v[1] = 'Arthur'
v[8] = 'Feijão', 'Jabuti'
print(d1)
print(v)

d1 = {
    1: 2,
    2: 3,
    4: 5,
}
d2 = {
    'a': 'b',
    'c': 'd',
}
print(d1)
print(d2)
d1.update(d2)
print(d1)