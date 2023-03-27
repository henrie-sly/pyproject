a = 'Hello'
b = 3
a *= b
print(a)

names = ["James", "John", "Alex"]
schools = ("UniAbuja", "UniBen", "UniLag")
place = "Berger Junction"
food = {"Rice", "Beans", "Spag"}
print("John" in names)
print('e' in place)
print("Rice" in food)
print("unilag" in schools)

g = 10
h = -25
i = 0.062
if g < h:
    print("Block 1")
elif h > g:
    print("Block 2")
elif i > h:
    print("Block 3")
elif h > i:
    print("Block 4")
else:
    print("Block 5")

z = 20
x = 10

if z > 10:
    if z == 10:
        print("Inner Block")
else:
    print("Outer Block")

