perguntas = {
    'Pergunta 1': {
        'Pergunta': 'Quanto é 1+2?',
        'Respostas': {'a': '1', 'b': '2', 'c': '3'},
        'Resposta_certa': 'b',
    },
    'Pergunta 2': {
        'Pergunta': 'Qual seu nome?',
        'Respostas': {'a': 'Arthur', 'b': 'Enzo', 'c': 'Lucas'},
        'Resposta_certa': 'a',
    },
}
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["Pergunta"]}')

    for rk, rv in pv['Respostas'].items():
        print(f'[{rk}]: {rv}')
    resposta_usuario = input('Resposta: ')
    print()
    