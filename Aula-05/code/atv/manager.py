import os


def cls():
    os.system('cls')


db = []


class Product():
    def __init__(self):
        pass

    def add(self, nome, preco, qnt):
        self._nome = nome
        self._preco = preco
        self._qnt = qnt

        obj = {
            'nome': self._nome,
            'preco': self._preco,
            'qnt': self._qnt
        }

        db.append(obj)

    def remove(self):
        cls()
        index = int
        search = input('Insira no nome: ')
        if search != '0':
            for i, obj in enumerate(db):
                if obj['nome'] == search:
                    print(db[i])
                    input()
                    index = i
        if search == '0':
            print('Voltar')

        print('Deseja deletar?\n'
              '1 - Sim\n'
              '2 - Não\n')
        res = input('Digite uma opção: ')

        if res == '1':
            if index != int:
                del db[i]
                print('Elemento deletado')
            else:
                print('Elemento invalido.')
        else:
            print('Voltar')

        input()

    def write(self):
        print(db)

    def update():
        pass

    def model(self):

        obj = {
            'nome': str,
            'preco': float,
            'qnt': int
        }

        self._obj = obj

        return obj


def add_obj(obj):
    print('Digite os seguintes atributos.')
    for key, value in obj.items():
        resp = value(input(f'{key}: '))
        obj[key] = resp
    return obj


def interface():
    while True:

        p = Product()

        print('Manager\n\n'
              '0 - Sair\n'
              '1 - Adicionar\n'
              '2 - Remover\n'
              '3 - Listar\n'
              '4 - Atualizar\n')
        opt = input('Escolha uma opção: ')
        if opt == '0':
            break

        if opt == '1':

            obj = add_obj(p.model())
            nome = obj['nome']
            preco = obj['preco']
            qnt = obj['qnt']
            p.add(nome, preco, qnt)
            print('Produto Adicionado.')
            input()

        if opt == '2':
            p.remove()
        if opt == '3':
            p.write()
            input()
        if opt == '4':
            pass


interface()
