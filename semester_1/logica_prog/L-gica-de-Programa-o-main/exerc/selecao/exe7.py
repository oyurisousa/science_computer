"""Escrever um programa que lê 4 valores: P, A, B e C. Se P=1 então calcular a média aritmética de A, B e C e escrever esta
média; se P=2 somar os 3 valores atribuindo este valor a uma variável qualquer e escrevendo esta soma; se P=3 fazer um
teste  para saber se B é par, se  é par escrever a mensagem e  o valor, caso contrário  escrever  que  é ímpar.  Se  for qualquer
outro valor mostrar a mensagem “operação inválida”."""

P = int(input("digite o valor P: "))
A = int(input("digite o valor A: "))
B = int(input("digite o valor B: "))
C = int(input("digite o valor C: "))

if P == 1:
    media = (A+B+C)/3
    print(media)
elif P == 2:
    soma = A + B + C
    print(soma)
elif P == 3:
    if B % 2 == 0:
        print(f"{B} é par")
    else:
        print(f"{B} é impar")
else:
    print("opção inválida")
