class Aluno:
    def __init__(self, nome, nota1, nota2):
        self._nome = nome
        self._nota1 = nota1
        self._nota2 = nota2

    def get_nome(self):
        return f'Olá {self._nome}'
    
    def get_notas(self):
        self._media = (self._nota1 + self._nota2) / 2
        return f' {self._media}'
    
a = Aluno('Aluno Random', 9, 8)

print(a.get_notas())