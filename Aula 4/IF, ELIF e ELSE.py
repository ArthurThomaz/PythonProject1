""" 
IF, ELIF e ELSE
"""""
# Ele le de cima para baixo, e para na primeira Verdadeira que encontra.
# Ignorando todos os seguintes independente se forem verdadeiros ou falsos.

if False:
    print("Isto é verdadeiro.")

elif True:
    print("Agora sim é verdadeiro.") # O Pyhton para de ler nesta linha, pois ela é verdadeira.

elif False:
    print("Esse é completamento falso.") # A partir dessa linha ele não le as informações, mesmo que sejam verdadeiras.
    print(75/5)

elif True:
    print("XESQUEDELE")
    nome = input('Qual o seu nome? ')
    print(f"O nome dele é {nome}")
else:
    print("FLAMENGO")