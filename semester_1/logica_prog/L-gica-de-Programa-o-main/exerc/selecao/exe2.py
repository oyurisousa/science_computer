"""Escrever um programa que leia três valores inteiros e apresente o menor dos valores lidos"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))

if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n3 and n2 < n1:
    print(n2)
elif n3 < n1 and n3 < n2:
    print(n3)
elif (n1 == n3) and n1 < n2:
    print(n1)
elif (n2 == n3) and n2 < n1:
    print(n2)
elif (n1 == n2) and n1 < n3:
    print(n1)
else:
    print("todos os valores são iguais.")
