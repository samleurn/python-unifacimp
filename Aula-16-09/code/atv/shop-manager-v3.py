class Empregado:
    def __init__(self, nome, salario_base):
        self._nome = nome
        self._salario_base = salario_base

    def calculo_salario(self):
        ...
    def mostra_salario(self, salario_final):
        self._salario_final = salario_final
        return f'O seu salário é de R$ {self._salario_final}.'


class Gerente(Empregado):
    def calculo_salario(self):
        bonus = self._salario_base * 0.2
        salario_final = self._salario_base + bonus
        self._salario_final = salario_final

    def mostra_salario(self):
        return super().mostra_salario(self._salario_final)


class Vendedor(Empregado):
    def calculo_salario(self, comissão):
        self._comissão = comissão
        valor_comissao = self._salario_base * comissão
        salario_final = self._salario_base + valor_comissao
        self._salario_final = salario_final
    def mostra_salario(self):
        return super().mostra_salario(self._salario_final)


g = Gerente('Welliton', 10000)
g.calculo_salario()
print(g.mostra_salario())

v = Vendedor('Pedro', 1515)
v.calculo_salario(0.01)
print(v.mostra_salario())
