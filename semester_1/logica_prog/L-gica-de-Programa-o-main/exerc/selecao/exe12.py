"""
Uma  cidade  classifica  um  índice  de  poluição  menor  que  35  como  agradável;  de  35  até  60  desagradável  e  acima  de  60
perigoso.  Escreva  um  programa  que  lê  um  número  real  representando  o  índice  de  poluição  e  imprime  a  classificação
adequada para ele
"""
indice = float(input("Digite o índice de poluição: "))
if indice < 35:
    print("Agradavel")
elif 60 >= indice >=35:
    print("Desagradável")
elif indice > 60:
    print("PERIGOSO!")
elif indice < 0:
    print("Valor inválido")