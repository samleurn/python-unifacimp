import json


class School:
    def __init__(self):

        aluno = {}

        self._aluno = aluno

    def cadastrar_aluno(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula

        self._aluno["nome"] = self._nome
        self._aluno["matricula"] = self._matricula

    def exibir_aluno(self):
        print(f"Aluno: {self._nome}, matricula: {self._matricula}")

    def notas_aluno(self, notas):
        self._notas = notas
        self._aluno["notas"] = self._notas

    def exibir_notas(self):
        i = 0
        print(f"Aluno: {self._aluno['nome']}")
        for a in self._aluno["notas"]:
            print(f"Nota {i+1}: {a}")
            i += 1
        # print(f'notas: {self._aluno['notas'][]}')

    def calcular_media(self):
        self._media = sum(self._notas) / len(self._notas)
        self._aluno["media"] = self._media

        msg = ""

        if self._media >= 6:
            msg = "aprovado"
        else:
            msg = "reprovado"

        self._situacao = msg
        self._aluno["situacao"] = self._situacao

    def exibir_media(self):
        self.calcular_media()
        print(
            f"Aluno: {self._aluno['nome']}, sua média é {self._aluno['media']} e voce está {self._situacao}"
        )

    def exibir_dados_aluno(self):
        dados = json.dumps(self._aluno, indent=4, separators=(",", ": "))
        print(f"Dados do Aluno: {dados}")


a1 = School()
a2 = School()
a3 = School()

a1.cadastrar_aluno("Welliton", "20250293")
a1.notas_aluno([7, 8, 9, 8])

a2.cadastrar_aluno("Ana", "20259874")
a2.notas_aluno([8, 9, 8, 9])

a3.cadastrar_aluno("Rebecca", "20254567")
a3.notas_aluno([4, 6, 3, 9])

print("\n------Alunos------\n")
a1.exibir_aluno()
a2.exibir_aluno()
a3.exibir_aluno()

print("\n------Notas-------\n")
a1.exibir_notas()
a2.exibir_notas()
a3.exibir_notas()

print("\n------Media-------\n")
a1.exibir_media()
a2.exibir_media()
a3.exibir_media()

""" print("\n------Dados-------\n")
a1.exibir_dados_aluno()
a2.exibir_dados_aluno() """
