print('----Conjuntos------------')
# Conjunto
print('----Set------------------')
conjunto = set()
print(type(conjunto))

# Set Nums
print('----Set-Nums-------------')
nums = {1,2,3,4,5}
print(nums)

# Itera Set
print('----Itera-Set------------')
for num in nums:
    print('----Value----')
    print(num)

# Union
print('----Union-Set------------')
nums1 = {1,2,3,4,5}
nums2 = {6,7,8,9,0}
numsUnion = nums1.union(nums2)
print(numsUnion)

# Remove Duplicate
print('----Duplic-Set------------')
allNums = {1,1,3,5,5,5,6,7,7,2,2,4}
print(allNums)
print('----Org-----')
numsOrg = set(allNums)
print(numsOrg)

# Set -> List
print('----Duplic-Set------------')
numsList = list(nums)
print(numsList)

# n lembro .-.
print('----;-;------------')
a = { x for x in range(1, 11) if x % 2 ==0}
print(a)
