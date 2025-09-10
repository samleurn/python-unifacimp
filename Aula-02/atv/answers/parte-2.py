cont = 0

def incrementar_contador():
    global cont
    cont = cont + 1
    msg = f'O numero global é {cont}'
    return msg

incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()

message = incrementar_contador()
print(message)
