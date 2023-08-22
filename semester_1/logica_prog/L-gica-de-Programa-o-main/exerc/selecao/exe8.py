"""Escreva um programa que lê as quatro notas de um aluno e calcula a média. O programa deve imprimir a média calculada e
uma  mensagem  indicando  se  o  aluno  foi  aprovado  ou  reprovado.  Um  aluno  é  aprovado  quando  este  obtém  uma  média
maior ou igual a 7,0"""
nome = input("Qual o seu nome ? ")
n1 = int(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))
n3 = int(input("Digite a nota 3: "))
n4 = int(input("Digite a nota 4: "))
situacao = True
media = (n1 + n2 + n3 + n4)/4

if media >= 7.0:
    situacao = "aprovado"
else:
    situacao = "reprovado"
print(f"O aluno {nome} obeteve a média {media}, portanto está {situacao}.")
