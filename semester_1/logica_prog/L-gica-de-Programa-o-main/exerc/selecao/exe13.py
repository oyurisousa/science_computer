"""
Escreva  um  programa  que  lê  a  média  semestral  de  um  aluno  e  imprime  o  conceito  atribuído  a  esta  média.  O  conceito  é
dado como segue:
Média Conceito 
10,0 ≤ média ≤ 9,0 A 
9,0 < média ≤ 8,0 B 
8,0 < média ≤ 7,0 C 
7.0 < média ≤ 5.5 D 
5,5 < média E 

"""
media = float(input("Qual foi sua média(0-10)? "))

if media >= 9 and media <= 10:
    print("conceito A")
elif media < 9 and media >= 8:
    print("conceito B")
elif media < 8 and media >= 7:
    print("conceito C")
elif media < 7 and media >= 5.5:
    print("conceito D")
elif media < 5.5 and media >= 0:
    print("conceito E")
else:
    print("por favor insira uma nota de 0 a 10")
    