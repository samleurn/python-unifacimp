def dia_semana(dia):
    if dia == 1:
        return "Domingo"
    elif dia == 2:
        return "Segunda-feira"
    elif dia == 3:
        return "Terça-feira"
    elif dia == 4:
        return "Quarta-feira"
    elif dia == 5:
        return "Quinta-feira"
    elif dia == 6:
        return "Sexta-feira"
    elif dia == 7:
        return "Sábado"
    else:
        return "Dia inválido"


def interface():
    while True:
        print("Menu:")
        print("1. Verificar dia da semana")
        print("2. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            dia = int(input("Digite um número (1-7) para o dia da semana: "))
            print(dia_semana(dia))
        elif escolha == '2':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


interface()
