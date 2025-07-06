'''
Operadores Lógicos
and, or, not
in e not in
'''''

"AND"
# Vai checar se a comparação 1 é verdadeira e se a comparação 2 TAMBÉM é verdadeira.
# # Caso alguma das comparações seja falsa, ele irá responder com false
# ( True and True ) = True
# ( True and False ) = False

comparação1 and comparação2

"OR"
# Vai checar se ALGUMA comparação é verdadeira.
# ( True or True ) = True
# ( True or False ) = True
# ( False or False ) = False

comparação1 or comparação2

"NOT"
# Inverte o valor
# Só precisa de uma expressão

a = 2
b = 3

if not b > a:
    print("B é maior do que A")
else:
    print("A é maior do que B")

"IN"

nome = "Arthur Thomaz Alves"

if "a" in nome:
    print("Existe a letra A no seu nome.")
else:
    print("Não existe essa letra em seu nome.")

