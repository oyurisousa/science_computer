import random 
lista1 = []
lista2 = []
listaResultante = []
x = 0
while x < 10:
    lista1.append(random.randint(0, 20))
    x += 1
print(lista1)
i = 0
for i in range(10):
    lista2.append(random.randint(0, 20))
print(lista2)
j = 0
for j in range(10):
    listaResultante.append(lista1[j]*lista2[j])
print(listaResultante)
