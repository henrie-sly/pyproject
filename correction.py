user_input = input('Enter list')

new_list = user_input.split('a')

result = []

for num in new_list:
    print(num.strip('l'))

print(result)
