def printaNotas(media):
    print(f'Sua media é {media}')

def calculadora(notas):
    n = 0
    for nota in notas:
        n = n + nota
        print(nota)

    return n / len(notas)

    
def get_notas():
    notas = []
    qnt = 0
    while qnt < 4:
        nota = input(f'Nota {qnt}: ')
        notas.append(nota)
        qnt = qnt + 1

    media = calculadora(notas)
    return media


def interface():

    while True:
        print('Deseja Calcular suas Notas?\n\n' \
        '1 - Sim\n' \
        '2 - Não\n')

        opt = input('Selecione uma opção: ')
        
        if opt == '1':
            msg = get_notas()
            print(msg)
            break
        if opt == '2':
            print('Tenha uma boa noite')
            break
        

interface() 