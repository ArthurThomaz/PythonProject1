from datetime import datetime
class pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não se fala enquanto esta comendo.')
            return
        if self.falando:
            print(f'{self.nome} esta falando.')
            return
        print(f'{self.nome} esta falando sobre {assunto}.')
        self.falando = False
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja esta comendo.')
            return
        print(f'{self.nome} esta comendo {alimento}.')
        self.comendo = True
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não esta comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade



