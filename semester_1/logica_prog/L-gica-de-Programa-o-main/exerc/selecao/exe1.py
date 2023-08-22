"""Escrever um programa que leia dois valores inteiros e apresente o maior dos valores lidos"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2

if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print("Os valores inseridos são iguais")
