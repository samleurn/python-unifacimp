# Class Filho
class Animal:
    def __init__(self, nome):
        self._nome = nome
        pass
    def emitirSom(self):
        ...

# Herança
class Cachorro(Animal):
    def emitirSom(self):
        return f'{self._nome} emite latido'

class Gato(Animal):
    def emitirSom(self):
        return f'{self._nome} emite miado'
    
a = Cachorro('Gato')
msg = a.emitirSom()
print(msg)