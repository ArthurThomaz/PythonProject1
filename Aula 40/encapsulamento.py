'''
public, protected, private
_ privado - protected = public with an _ before 
__ privado - mais forte ( _classname__attributename )
'''''

class database: # PUBLIC
    def __init__(self):
        self.dados = {}
    def insert_client(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})
    def client_list(self, id):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)
    def erase_client(self, id):
        del self.dados['clientes'][id]
db = database()
db.insert_client(1, 'Arthur')
db.insert_client(2, 'Joao')
db.insert_client(3, 'Maria')
db.erase_client(3)
db.client_list(id)
print(db.dados)


class database:  # PRIVATE
    def __init__(self):
        self.__dados = {}
    def insert_client(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    def client_list(self, id):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    def erase_client(self, id):
        del self.__dados['clientes'][id]
db = database()
db.insert_client(1, 'Arthur')
db.insert_client(2, 'Joao')
db.__dados = 'Another'
print(db.__dados)
print(db._database__dados)