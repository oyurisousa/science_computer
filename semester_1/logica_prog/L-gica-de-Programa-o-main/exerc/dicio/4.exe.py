import os
aprov = {'gols': {}}
jogadores = []
while True:
    aprov = {'gols': {}}
    aprov["nome"] = input("qual o seu nome? ")
    aprov["quant_part"] = int(input("quantas partidas você jogou? "))
    print("digite a quantidade de gols em cada partida:")
    for x in range(aprov["quant_part"]):
        aprov['gols'][f"partida_{x+1}"] = int(input(f"partida {x+1}: "))
    jogadores.append(aprov.copy())
    aprov.clear()
    boo = input("Deseja cadastarar outro jogador?(1-sim,0-não)? ")
    if boo == "0":
        os.system("clear")
        break
    else:
        os.system("clear")
def Dados(i):
    
    #visualização dos dados dos jogadores
    print("=="*30)
    print(f"Nome : {jogadores[i]['nome']}")
    print(f"Total de partidas jogadas: {jogadores[i]['quant_part']}")
    print("--"*15)
    print(f"Gols por partida:")
    for x in range(jogadores[i]["quant_part"]):
        print(f"Partida {x+1} : {jogadores[i]['gols'][f'partida_{x+1}']}")

while True:
    print("##"*30)
    print("Lista de jogadores por ordem de cadastro: ")
    print("0 - nenhum")
    print("1 - todos")
    for x in range(len(jogadores)):
        print(f"{x + 2} - {jogadores[x]['nome']}")
    sel = 0
    sel = int(input(f"\nPara ver os dados, digite o numero do jogador correspondente: "))
    os.system("clear")
    if sel == 0:
        print("nenhum jogador escolhido!")
        break
    elif sel > 1:
        sel = sel - 2
        Dados(sel)
    elif sel == 1:
        for x in range(len(jogadores)):
            Dados(x)
        print("")
    else:
        print("digito inválido, tente novamente!")
