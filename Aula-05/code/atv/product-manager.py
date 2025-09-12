import os
import json

db = []

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def title():
    print('Maneger\n')

def press_enter():
    input('Press Enter to Continue: ')

def mid():
    while True:
        cls()
        title()
        print('Deseja Adicionar um Produto?\n\n' \
                '1 - Sim\n' \
                '2 - Não\n')
        opt = input('Selecione uma opção: ')

        if opt == '1':
            add()
            break
        if opt == '2':
            interface()
            break
        else:
            print('Opção Invalida')
            input()

def add():

    cls()

    obj = model()

    title()
    print('Digite os seguintes atributos\n')

    for key, value in obj.items():
        if key == 'id':
            pass
        else:
            atr = value(input(f'{key}: '))
            obj[key] = atr

    db.append(obj)

    press_enter()
    mid()

def val_remove():
    print('Tem certeza?')
    

def revome():
    while True:
        cls()
        title()

        print('Digite o id do item que deseja remover.\n')
        
        remv = input('Id do item: ')
        i = int(remv)
        if remv != '':
            val_remove()
            del db[i]
            
        else:
            print('Digite um nome válido')

        press_enter()

def update():
    print('update')
    press_enter()

def write():
    cls()
    title()
    print(f'{db}\n')
    press_enter()

def model():
    obj = {
        'id': int,
        'nome': str,
        'preco': float,
        'quantidade': int
    }
    return obj

def interface():
    while True:
        cls()

        title()

        print('1 - Adicionar\n' \
            '2 - Remover\n' \
            '3 - Listar\n' \
            '4 - Atualizar\n' \
            '5 - Sair\n')
        opt = input('Digite uma opção: ')
        
        if opt == '1':
            mid()
            break
        if opt == '2':
            revome()
            break
        if opt == '3':
            write()
        if opt == '4':
            update()
        if opt == '5':
            break

interface()

