class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def get_nome(self):
        return f'Olá {self._nome}.'
    
    def get_idade(self):
        return f'Você tem {self._idade}.'
    
    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def set_idade(self, novo_idade):
        self._idade = novo_idade

p = Pessoa('Sam', 20)
print(p.get_nome())
print(p.get_idade())

p.set_nome('Alan')
p.set_idade(18)
print(p.get_nome())
print(p.get_idade())

p.set_nome('Hello')
p.set_idade(100)
print(p.get_nome())
print(p.get_idade())