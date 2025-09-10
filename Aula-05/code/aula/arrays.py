print('----------Arrays----------')
# Numbers
print('-----------Type-----------')
nums = [1,2,3,4,5]
print(type(nums))

# Strings
print('----------Arr-Str----------')
names = ['Alice', 'Ricardo', 'Wellinton']
print(names)

# Mixed
print('---------Arr-Mixed----------')
mixedValues = [1,'Python', 3.14, True]
print(mixedValues)

# Pega o valor por indice
print('--------Value-Index---------')
firstValue = nums[0]
print(firstValue)

# Adiciona no final
print('--------Adiciona-Arr--------')
nums.append(10)
print(nums)

# Substitui
print('------------Sum---------')
nums[2] = 20
print(nums)

# Remove o valor especificado
names.remove('Ricardo')
print(names)
print('--------Remove--------------')

# len() pega a qnt de itens no array
qnt_nomes = len(names)
print(qnt_nomes)
print('--------Length-------------')

# for var in array <- estrutura
print('--------For--------------')
for name in names:
    print(name)
    print('-----------')

# .find do py
print('--------Find-------------')
namePeople = 'Wellinton'
if namePeople in names:
    print('Find!') 
else:
    print('Nah!') 

# Ordena em crescente
print('--------Sort--------------')
nums.sort()
print(nums)

# Valor minimo
print('----------Min-------------')
minNums = min(nums)
print(minNums)

# Valor maximo
print('-----------Max-----------')
maxNums = max(nums)
print(maxNums)

# Somar os valores
print('---------Soma-------------')
sumNums = sum(nums)
print(sumNums)

# Deleta
print('---------Deleta-----------')
del nums[2]
print(nums)

# Iverte a ordem dos valores
print('--------Inverter----------')
nums.reverse()
print(nums)

# Instanciar
print('--------Instanciar----------')
lista = []
print(lista)
