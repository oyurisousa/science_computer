import random 
lista = []
x = 0
while x < 50:
    lista.append(random.randint(1,50))
    x += 1
print(lista)

i = 0
j = 49
while i < j:
    lista[i],lista[j] = lista[j], lista[i]
    i += 1
    j -= 1
print(lista)