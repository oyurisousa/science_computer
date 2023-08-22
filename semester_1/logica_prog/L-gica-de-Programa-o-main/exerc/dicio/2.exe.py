from random import randint
jogadores = {}
lista = []
maior = []
x = 0
for i in range(4):
    nome = input(f"jogador {x+1}: ")
    x = randint(1,6)
    print(f"{nome} você obteve o numero {x}")
    jogadores.update({nome : x})
    
lista.sort()
print(lista)
print(jogadores)
print("o vencedor foi ")