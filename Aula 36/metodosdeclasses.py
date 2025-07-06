class pessoa:
    ano_atual = 2025
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    @classmethod
    def set_ano_nascimento(cls,nome , ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
p1 = pessoa.set_ano_nascimento('Arthur', 2000)
# p1 = pessoa('Arthur', 24) 
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()