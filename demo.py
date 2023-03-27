a = 10
b = 20
c = 9
d = 10
if a > d:
    print("The first")
elif c > d:
    print("The second")
elif (d > c) & (c < b):
    print("The third")
elif (d == a) | (d > c):
    print("The fourth")
else:
    print("last")

