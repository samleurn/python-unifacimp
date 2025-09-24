import os


def cls():
    os.system('cls')


def dividir(x, y):
    if y == 0:
        raise ValueError("Não é possivel dividir por zero.")
    else:
        return x / y


def calculator():

    try:
        while True:
            cls()
            print('Calculadora\n')
            print('1 - Dividir')
            print('2 - Sair')
            opt = input('Selecione: ')
            if opt == '1':
                x = input('Digite o primeiro numero: ')
                y = input('Digite o segundo numero: ')
                resultado = dividir(float(x), float(y))
                print(resultado)
                input()

            elif opt == '2':
                print('Fechando o Sistema')
                input()
                break
            else:
                print('Opção invalida')
                input()

    except ValueError as e:
        print(f'Erro: {e}')

calculator()