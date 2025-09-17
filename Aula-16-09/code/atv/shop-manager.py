class Empregado:
    def __init__(self, nome, salario_base):
        self._nome = nome
        self._salario_base = salario_base

    def calculo_salario(self):
        ...

    def mostra_salario(self, salario):
        self._salario = salario
        return f'Seu salário é de R$ {self._salario}.'


class Gerente(Empregado):
    def __init__(self):
        self._bonus = 0.2
    def calculo_salario(self):
        salario_bonus = self._salario_base * self._bonus
        salario_final = self._salario_base + salario_bonus
        self._salario_final = salario_final

    def mostra_salario(self):
        return super().mostra_salario(self._salario_final)


class Vendedor(Empregado):
    def __init__(self):
        self._imposto = 0.3
    def calculo_salario(self, comissão):
        self._comissão = comissão

        salario_beneficio = self._salario_base * self._comissão
        salario_bruto = self._salario_base + salario_beneficio
        salario_final = salario_bruto - self._imposto

        self._salario_final = salario_final

    def mostra_salario(self):

        return super().mostra_salario(self._salario_final)


g = Gerente('Welliton', 10000)
g.calculo_salario()
msg = g.mostra_salario()
print(msg)

v = Vendedor('Pedro', 1515)
v.calculo_salario(0.01)
salario_vendedor = v.mostra_salario()
print(salario_vendedor)
