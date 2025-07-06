from random import randint
class pessoa:
    ano_atual = 2025
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    @classmethod # Referente a classe (pessoa)
    def set_ano_nascimento(cls,nome , ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    @staticmethod # Dentro dele não pode usar self=(instancia) nem cls=(classe)
    def gera_id():
        rand = randint(100, 999)
        return rand
p1 = pessoa.set_ano_nascimento('Arthur', 2000)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(pessoa.gera_id()) # Para utilizar o static method pegamos com instancia ou classe.
print(p1.gera_id()) # Mas para altera-lo não.
