class Empregado:
    def __init__(self, nome, salario_base):
        self._nome = nome
        self._salario_base = salario_base

    def calculo_salario(self):
        ...


class Gerente(Empregado):
    def calculo_salario(self):
        bonus = self._salario_base * 0.2
        salario_final = self._salario_base + bonus
        return f'Seu salário é de R$ {salario_final}.'


class Vendedor(Empregado):
    def calculo_salario(self, comissão):
        self._comissão = comissão
        valor_comissao = self._salario_base * comissão
        salario_final = self._salario_base + valor_comissao
        return f'Seu salário é de R$ {salario_final}.'


g = Gerente('Welliton', 10000)
salario_gerente = g.calculo_salario()
print(salario_gerente)

v = Vendedor('Pedro', 1515)
salario_vendedor = v.calculo_salario(0.01)
print(salario_vendedor)
