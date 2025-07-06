logged_user = False
if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'
print(msg)

msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
print(msg)

idade = input('Digite sua idade: ')
idade = int(idade)
e_de_maior = idade >= 18
msg = 'Pode acessar.' if e_de_maior else 'Não pode acessar.'
print(msg)