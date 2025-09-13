import os

import json


def cls():
    os.system('cls')


estoque = []


class Product():
    _code = 0

    def __init__(self):
        pass

    def add(self, nome, preco, qnt):

        Product._code += 1
        self._code = Product._code
        self._nome = nome
        self._preco = preco
        self._qnt = qnt

        obj = {
            'code': self._code,
            'nome': self._nome,
            'preco': self._preco,
            'qnt': self._qnt
        }

        estoque.append(obj)

        print(f'Produto Adicionado: {obj}')
        input()

    def remove(self, index):
        if index != None:
            del estoque[index]
        print('Elemento deletado')

    def write(self):
        cls()
        print('Manager\n')
        print(f'Estoque:\n {json.dumps(estoque, indent=4)}')
        input()

    def update(self, index, produto):

        if index != None:
            estoque[index] = produto

            print(f'Produto Alterado {produto}')
            input()
        else:
            print('Produto Invalido')

    def model(self):
        obj = {
            'nome': str,
            'preco': float,
            'qnt': int
        }

        self._obj = obj
        return self._obj


def add_obj(obj):
    cls()

    print('Manager\n')
    print('Digite os seguintes atributos.')

    prod = None
    atr = None

    for key, value in obj.items():

        inpt = input(f'{key}: ')

        if inpt == '':
            if value == str:
                prod = ''
            if value == int or value == float:
                prod = 0
            atr = prod
        else:
            atr = value(inpt)
        obj[key] = atr

    return obj


def search(inpt):

    index = None

    if inpt == '' or inpt == '0':
        return '0'
    if isinstance(int(inpt), int):
        for i, obj in enumerate(estoque, start=0):
            if obj['code'] == int(inpt):
                return i
    else:
        return '0'


def remove_obj(obj):
    cls()

    print('Manager\n')
    print('0 - Voltar\n')
    inpt = input('Digite o código: ')
    rsp = search(inpt)

    if rsp == '0':
        print('Voltar')
    else:
        i = rsp
        print(f'Item: {estoque[i]}')
        print('Deseja deletar?\n'
              '1 - Sim\n'
              '2 - Não\n')
        res = input('Digite uma opção: ')
        if res == '1':
            if i != int:
                print(rsp)
                return i
            else:
                print('Elemento invalido.')
        else:
            print('Voltar')

    input()


def uptdate_obj():
    cls()

    print('Manager\n')
    print('0 - Voltar\n')
    inpt = input('Digite o código: ')
    index = search(inpt)

    if index == '0':
        print('Voltar')
    else:
        if index != int:
            atr = None
            obj = estoque[index]
            print('Digite os novos valores\n'
                  'obs.: Para pular a modificação pressione enter: ')
            for key, value in obj.items():
                if key != 'code':
                    inpt = input(f'{key}: ')
                    if inpt == '':
                        atr = value
                    else:
                        if isinstance(value, float):
                            atr = float(inpt)
                        elif isinstance(value, int):
                            atr = int(inpt)
                        elif isinstance(value, str):
                            atr = str(inpt)
                        else:
                            print('Valor invalido.')

                    obj[key] = atr
            return {'index': index, 'obj': obj}
        else:
            print('Produto não encontrado')


def interface():
    while True:
        cls()

        p = Product()
        model = p.model()

        print('Manager\n\n'
              '0 - Sair\n'
              '1 - Adicionar\n'
              '2 - Remover\n'
              '3 - Listar\n'
              '4 - Atualizar\n')
        opt = input('Escolha uma opção: ')
        if opt == '0':
            print('Boa noite!')
            break

        if opt == '1':

            obj = add_obj(model)
            nome = obj['nome']
            preco = obj['preco']
            qnt = obj['qnt']
            p.add(nome, preco, qnt)

        if opt == '2':
            index = remove_obj(model)
            p.remove(index)

        if opt == '3':
            p.write()

        if opt == '4':
            resp = uptdate_obj()
            index = resp['index']
            obj = resp['obj']
            p.update(index,  obj)


interface()
