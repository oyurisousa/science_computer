produtos = []
estoque = []
baixo_estoque = []
quant_produtos = int(input(f"quantos produtos você deseja cadastrar? "))
for x in range(quant_produtos):
    print("------------------------------")
    produtos.append(input(f"Nome do produto {x+1}: "))
    estoque.append(int(input(f"Numero de estoque: ")))
    if estoque[x] < 5:
        baixo_estoque.append(x)
print()
print(f"Produtos = {produtos}")
print("-------------------------------")
print("produtos com estoque baixo(<5)")
for x in range(len(baixo_estoque)):
        print(f"{produtos[baixo_estoque[x]]} = {estoque[baixo_estoque[x]]}")