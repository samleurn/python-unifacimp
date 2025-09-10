# Obj ou Dict
print('----Dict-------------------------')
dictionary = {
    "nome": "Wellition",
    "idade": 33,
    "cidade": "Imperatriz"
}
print(dictionary)

# Acessando Chave
print('----Accss-Key--------------------')
key = "idade"
valor = dictionary[key]
print(key, valor)

# Modificando Chave
print('----Modify-Key--------------------')
key = 'cidade'
dictionary[key] = 'São Luiz'
valor = dictionary[key]
print(key, valor)

# Adiciona Chave
print('----Add-Key--------------------')
key = 'profissao'
dictionary[key] = 'dev'
valor = dictionary[key]
print(key, valor)

# Deletar Chave
print('----Delete-Key--------------------')
key = 'nome'
del dictionary[key]
valor = dictionary
print(key, valor)

# Iterar Obj
print('----Itera-Obj--------------------')
for key in dictionary:
    print('----value----')
    print(key, dictionary[key])

print('----Itera-Obj-V2------------------')
for key, valor in dictionary.items():
    print('----value----')
    print(key, valor)
