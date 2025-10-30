#№1

a = (1, 2, 3, 4)
b = (1, 2, 5, 4)
print(len(a))
print(len(b))
print(list(zip(a, b)))
for i, j in zip(a, b):
    print(i, j)
#№2

app1 = {"anna", "max", "olya", "ivan", "dima"}
app2 = {"olya", "stepan", "max", "ira"}
print(app1.intersection(app2))
print(app1.difference(app2))
print(app1.union(app2))
#№3

chat = {"anna", "max", "olya", "ivan", "dima"}
ban = {"olya", "stepan", "max", "ira"}
ban2 = set(ban)
chat -= ban2
print(len(chat))
print(chat)
# #№4

a = ["45", "92", "16", "100"]
result = [int(i[0]) for i in a]
print(result)
#№5

x = [1, 5, 9]
y = [4, 2, 7]
print(list(zip(x,y)))