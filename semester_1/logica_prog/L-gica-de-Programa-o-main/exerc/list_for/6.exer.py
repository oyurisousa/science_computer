nivel_minimo = int(input("Qual o numero minimo por peça antes de entar em esqoque baixo?"))
filiais = ["norte", "sul", "central", "py & cia", "cia do python"]  
pecas  =  ["fio 10",  "parafuso",  "porca",  "arruela",  "cola",  "cabo flat", 
"botão", "led laranja", "led vermelha", "circuito"]  
estoques = [[173, 87, 82, 177, 24, 175, 193, 176, 98, 78], [13, 298, 512, 17, 214, 58, 195, 187, 187, 129], [16, 97, 88, 71, 224, 175, 935, 86, 112, 100],[167, 279, 218, 217, 46, 158, 35, 106, 230, 212], [73, 187, 132, 77, 224, 582, 135, 76, 176, 178]]
lista = []


for x in range(len(filiais)):
    print("================================================")
    print(filiais[x].upper())
    print("================================================")
    for i in range(len(pecas)):
        if estoques[x][i] < nivel_minimo:
            print(f"{pecas[i]}...............{estoques[x][i]}")
'''
filiais = []
pecas = []
estoques = []
quant_pecas = int(input("Quantidade total de peças? "))
for x in range(quant_pecas):
    pecas.append(input(f"nome da peça {x+1}: "))
print("-----------------------------")
quant_filiais = int(input("quantas filiais? "))
for x in range(quant_filiais):
    print("===================================")
    filiais.append(input(f"Nome da filial {x + 1}: "))
    for i in range(quant_pecas):
        lista.append(int(input(f"quantidade de {pecas[i]}: ")))
    estoques.append(lista)
    lista = []

for x in range(len(filiais)):
    print("================================================")
    print(filiais[x].upper())
    print("-"*len(filiais[x]))
    for i in range(len(pecas)):
        if estoques[x][i] < nivel_minimo:
            print(f"{pecas[i]}...............{estoques[x][i]}")
'''