soma = lambda x , y: x+y
result = soma(3, 5)
print(result)

names_list = ['Wellinton', 'Ricardo', 'Ana', 'Beatriz', 'Carlos']
names_list_sorted = sorted(names_list, key=lambda name: len(name))
print(names_list_sorted)

num_list = [1,2,3,4,5,6,7,8,9]
par_nums = list(filter(lambda x: x % 2 == 0, num_list))
print(par_nums)


num_map = [1,2,3,4,5,6,7,8,9]
exp = list(map(lambda x : x ** 2, num_map))
print(exp)