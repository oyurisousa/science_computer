x = True
print("Digite numeros válidos de 1 a 12 ou 0 para parar")
while x >= 0:
    x = int(input("mes: "))
    if x == 1:
        print("janeiro")
    elif x == 2:
        print("fevereiro")
    elif x == 3:
        print("março")
    elif x == 4:
        print("abril")
    elif x == 5:
        print("maio")
    elif x == 6:
        print("junho")
    elif x == 7:
        print("julho")
    elif x == 8:
        print("agosto")
    elif x == 9:
        print("Setembro")
    elif x == 10:
        print("Outubro")
    elif x == 11:
        print("Novembro")
    elif x == 12:
        print("Dezembro")
    elif x == 0:
        break
    else:
        print("por favor digite um numero inteiro válido(0 a 12)")
    
