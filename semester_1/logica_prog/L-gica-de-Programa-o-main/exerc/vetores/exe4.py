import random 
lista = []
x = 0
while x < 80:
    lista.append(random.randint(1,80))
    x += 1
print(lista)
i = 0
j = 1
menor = lista[0]
while i < 80:
    if lista[i] < menor:
        menor = lista[i]
        
    i += 1
    j += 1
print(menor)