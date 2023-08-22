meta = int(input("qual a meta do mês? "))
quant_vendedores = int(input("quantos vendedores? "))
nome_vendedores = []
valor_vendas = []
true_meta = []
porcentagem = []
false_meta = []
for x in range(quant_vendedores):
    nome_vendedores.append(input(f"Vendedor {x+1}: "))
    valor_vendas.append(int(input(f"vendas total de {nome_vendedores[x]}: ")))
    porcentagem.append(valor_vendas[x]*100/meta)
    if valor_vendas[x] >= meta:
        true_meta.append(x)
    else:
        false_meta.append(x)
   
print("----------------------------")
print(f"{100*(len(true_meta))/quant_vendedores:.2f}% dos vendedores atingiram a meta, totalizando {len(true_meta)} vendedores")

print("------------------------------------")
print("vendedores que atingiram a meta: ")
for x in range(len(true_meta)):
    print(f"{nome_vendedores[true_meta[x]]}")

print("-------------------------------")
print("vendedores que atingiram a meta: ")
for x in range(len(true_meta)):
    print(f"{nome_vendedores[true_meta[x]]} = R${valor_vendas[true_meta[x]]} = {porcentagem[true_meta[x]]:.2f}%")

print("-------------------------------")
print("vendedores que não atingiram a meta")
for x in range(len(false_meta)):
    print(f"{nome_vendedores[false_meta[x]]}, seja mais produtivo!")
