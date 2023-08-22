import random 
lista = []
lista1 = []
x = 0
while x < 50:
    lista.append(random.randint(-99,99))
    x += 1
print(lista)
i = 0 
while i < 50:
    if lista[i] > 0:
        lista1.append(lista[i])
    i += 1

print(lista1)    
