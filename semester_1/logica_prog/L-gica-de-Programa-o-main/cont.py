from time import sleep
def contador(inicio=0,fim=0,passo=0):
    for x in range(1,11):
        print(x,flush=True)
        sleep(0.1)
    print("-"*30)
    for x in range(10,-1,-2):
        print(x,flush=True)
        sleep(0.1)
    print("-"*30)
    fim += 1
    if inicio > fim:
        passo = passo*(-1)
        fim  = fim - 2
    for x in range(inicio,fim,passo):
        print(x,flush=True)
        sleep(0.1)

inicio = int(input("digite inicio: "))
fim = int(input("digite fim: "))
passo = int(input("digite passo: "))
contador(inicio,fim,passo)