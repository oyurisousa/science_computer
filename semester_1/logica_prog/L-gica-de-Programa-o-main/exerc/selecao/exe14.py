"""
Escreva  um programa que lê 3 números inteiros e verifique  se estes podem formar  um triângulo,  ou seja, a soma de dois 
lados  tem  que  ser  necessariamente  maior  que  o  terceiro  lado.  Caso  os  valores  formem  um  triângulo,  verificar  se  é  um 
triângulo  eqüilátero  (3 lados  iguais),  isósceles  (2 lados iguais)  ou  escaleno (3 lados  diferentes).  Imprima  uma  mensagem 
conforme o resultado obtido
"""
print('TRIÂNGULO')
l1 = float(input("Digite o lado 1: "))
l2 = float(input("Digite o lado 2: "))
l3 = float(input("Digite o lado 3: "))
if (l1+l2) > l3 and (l1+l3) > l2 and (l2 + l3) > l1:
    if l1 == l2:
        if l2 == l3:
            print("Um triângulo Equilátero")
        else:
            print("Um triângulo isósceles")
    elif l1 == l3:
        print("Um triângulo isósceles")
    elif l1 != l2:
        if l2 == l3:
            print("Um triângulo isósceles")
        else:
            print("Um triângulo escaleno")        
else:
    print("Para ser um triângulo, a soma de dois lados  devem ser necessariamente  maior  que  o  terceiro  lado)
