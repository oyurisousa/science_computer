""" 
Escrever  um  programa  que  leia  um  número  real  fornecidos  pelo  usuário  e  calcule  sua  raiz  quadrada.  O  programa  deve
evitar calcular a raiz de um número negativo
"""
valor = int(input("digite um número: "))
if valor < 0:
    print(TypeError("Não existe raiz de um numero real dentro do conjunto dos reais"))
else:
    raiz = valor**(1/2)
    print(f"a raiz de {valor} é {raiz}")
