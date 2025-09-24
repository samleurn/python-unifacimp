import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter():
    input("Pressione Enter para continuar...")

def query():
    try:
        num = int(input("Digite um número: "))
        resultado = 10 / num
        print(f"Resultado da divisão: {resultado}")
        press_enter()
    except (ValueError, ZeroDivisionError)as e:
        print(f"Erro: {e}")
        press_enter()

def input_text():
    try:
        texto = input("Digite um texto: ")
        if not texto:
            raise ValueError("Texto não pode ser vazio")
        print(f"Você digitou: {texto}")
        press_enter()
    except (ValueError, TypeError) as e:
        print(f"Erro: {e}")
        press_enter()

def interface():
    while True:
        cls()
        print("Menu:")
        print("1. Fazer uma consulta")
        print("2 - Digitar um texto")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            query()
        elif escolha == '2':
            input_text()
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

interface()