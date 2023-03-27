my_list = []

result = [i for i in my_list if (i % 2) == 0] 

print(result)

a = [4,5,6,7,8,10,12,23,45,65,32,45,34,24]

result = [i for i in a if i % 2 != 0]
result = set(result)
result = list(result)
result.sort()
print(result)