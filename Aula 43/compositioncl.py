class Cliente:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.adress = []
    def insere_endereco(self, cidade, estado):
        self.endereco.append(Endereco(cidade, estado))
    def list_enderecos(self):
        for endereco in self.endereco:
            print(endereco.cidade, endereco.estado)
class Endereco:
    def __init__(self, cidade, estado):
        self.city = cidade
        self.state = estado