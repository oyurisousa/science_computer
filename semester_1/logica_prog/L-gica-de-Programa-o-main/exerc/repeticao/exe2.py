"""Escreva um programa que imprima os N primeiros números naturais ímpares"""  

#while
"""q = int(input("quantos números impares você quer imprimir? "))
x = 0
cont = 0
while cont < q:
    if x % 2 == 1:
        cont += 1
        print(x)
    x += 1
"""
#for  
q = int(input("quantos números impares você quer imprimir? "))
q = q * 2
for x in range(1,q,2):
    print(x)
