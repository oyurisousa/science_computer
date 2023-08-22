"""
Em uma disciplina são realizadas quatro provas. As duas primeiras notas tem peso 1 e as duas últimas peso 2. O aluno que 
obtém média 7,0 ou superior é aprovado. Se a média for inferior a 7,0 e superior ou igual a 2,5 o aluno está de exame final. 
Se a média for inferior a 2,5 o aluno está reprovado. Além das notas é considerada também a freqüência do aluno que deve 
ser  maior  ou igual  a  75%  para  que  ele  não  reprove  por  falta.  Faça  um  programa  que  lê a  freqüência  do  aluno,  o  número 
total  de  aulas  e  as  quatro  notas,  calcule  a  média  e  imprima  junto  com  uma  mensagem  que  indique  a  situação  do  aluno: 
“aprovado”, “exame final”, “reprovado por nota” ou “reprovado por falta”
"""
aulasTotal = int(input("Quantas aulas você teve? "))
aulasPlay = float(input("Quantas aulas você participou? "))
freq = (100 * aulasPlay) / aulasTotal

n1 = 0
n2 = 0
n3 = 0
n4 = 0
media = 0

if freq >= 75:
    n1 = float(input("Sua nota 1: "))
    n2 = float(input("Sua nota 2: "))
    n3 = float(input("Sua nota 3: "))
    n4 = float(input("Sua nota 4: "))
    media = (n1 + n2 + (n3*2) + (n4*2)) / 6
    if media >= 7 and media <= 10:
        print("Aprovado por média")
    elif media < 7 and media >= 2.5:
        print("Exame final")
    elif media < 2.5 and media >= 0:
        print("Reprovado por média")
    else:
        print("revise suas notas, elas devem ir de 0 até 10")
else:
    print("reprovado por falta")
