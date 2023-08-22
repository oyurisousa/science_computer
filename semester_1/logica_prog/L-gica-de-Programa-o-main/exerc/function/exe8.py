import os
def ficha(nome = "indefinido",quant_gols = "indefinido"):
    print(f"Nome: {nome}")
    print(f"Gols: {quant_gols}")
    
    
def execute():
    nome = input("Digite seu nome: ")
    gols = input("Quantidade de gols: ")
    os.system("clear")
    if nome == "":
        nome = "indefinido"
    if gols == "":
        gols = "indefinido"
    ficha(nome,gols)
    branch = input("deseja continuar?")
    os.system("clear")
    if branch in ("sim","s","Sim","S","SIM"):
        
        execute()
    else:
        print("Fim!")
        return

execute()