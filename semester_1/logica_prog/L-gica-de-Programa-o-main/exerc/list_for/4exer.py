quant_produtos = int(input("quantos produtos? "))
nome_produtos = []
vendas_2021 = []
vendas_2022 = []
porcentagem = []
dife_2022_2021 = []
space = 0
for x in range(quant_produtos):
    nome_produtos.append(input(f"produto {x+1}: "))
    vendas_2021.append(int(input(f"vendas de {nome_produtos[x]} em 2021: ")))
    vendas_2022.append(int(input(f"vendas de {nome_produtos[x]} em 2022: ")))
    dife_2022_2021.append(vendas_2022[x] - vendas_2021[x])
    porcentagem.append(dife_2022_2021[x] * 100/vendas_2021[x])
print("---------------------")
print("produtos que tiveram no ano de 2022 mais vendas do que no ano de 2021:")
for x in range(quant_produtos):
    space = (20 - len(nome_produtos[x]))* ".."
    space2 = (15 - len(str(vendas_2021[x]))) * ".."
    space3 = (15 - len(str(vendas_2022[x]))) * ".."
    if vendas_2022[x] > vendas_2021[x]:
        print(f"{nome_produtos[x]}{space}{vendas_2021[x]}{space2}{vendas_2022[x]}{space3}{porcentagem[x]:.2f}%")
