import os #para limpar a tela
from datetime import date 


clientes = []
idades  = []
sexo = {"M" : [], "F" : [], "N" : []}
cad = {}

while True:
    #dados do usuário
    cad['nome'] = input("Qual o seu nome? ")
    cad['sexo'] = input('Sexo(M,F,N): ')
    cad['datNasc'] = input('Data de nascimento(dd/mm/yyyy): ')
    anoNasc = int(cad['datNasc'][-4:])
    
    cad['idade'] = date.today().year - anoNasc # calcular idade
    idades.append(cad['idade'])
    clientes.append(cad.copy())
    
    #verificar o sexo e armazenar na lista correspondente
    if cad['sexo'] == "m" or cad['sexo'] == "M":
        sexo["M"].append(cad["nome"])
    elif cad['sexo'] == "f" or cad['sexo'] == "F":
        sexo["F"].append(cad["nome"])
    elif cad['sexo'] == "N" or cad['sexo'] == "n":
        sexo["N"].append(cad["nome"])

    cad.clear()
    boo = input("0 para sair e 1 para cadastrar outra pessoa: ")
    if boo == "0":
        os.system("clear")
        break
    else:
        os.system("clear")


mediaIdade = sum(idades) / len(clientes)
acimaMedia = []
for x in range(len(clientes)):
    if clientes[x]['idade'] > mediaIdade:
        acimaMedia.append(clientes[x]['nome'])

print("=="*20)
print("RELAÇÃO GERAL")
print("=="*20)
print(f"Quantidade de pesoas: {len(clientes)}")
print("--"*20)
print(f"Média geral em relação às idades: {mediaIdade:.2f}")
print("--"*20)
print("Relação de pessoas por sexo:")
print("#Masculino#")
for x in sexo["M"]: print(x)
print("#Feminino#")
for x in sexo["F"]: print(x)
print("#Não informado#")
for x in sexo["N"]:    print(x)
print("--"*20)

print(f"Relação de pessoas acima da média:")
for x in acimaMedia:
    print(x)

