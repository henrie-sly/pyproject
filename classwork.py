a = [4,5,6,7,8,9,10,13,14,18,19,28,30]
result = []

for i in a:
    if i > 1:
        for value in range(2, int(i/2)+1):
            if(i % value) == 0:

                break
            else:
                result.append(i)

result = set(result)
result = list(result)
print(result)


        