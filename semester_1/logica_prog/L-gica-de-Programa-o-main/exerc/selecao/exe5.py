"""Escrever  um  programa  que  leia  2  valores  inteiros  a  e  b  e  os  apresente  com  a  mensagem  "são  múltiplos"  ou  "não  são múltiplos" """
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 % n2 == 0:
    print(f"{n1} e {n2} são múltiplos")
else:
    print(f"{n1} e {n2} não são múltiplos")
