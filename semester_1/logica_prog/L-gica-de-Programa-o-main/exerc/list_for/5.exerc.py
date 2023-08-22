meta = 1000  
vendas = [["joao", 1673],["maria", 987],["jose", 8812],["ana", 177],["ivo", 224],["eva", 1758], ["ely", 1935], ["dalva", 876]] 
meta_atingida = []
print("----------------------------")
for x in range(len(vendas)):
    if vendas[x][1] > meta:
        meta_atingida.append(vendas[x])
print(f"{len(meta_atingida)*100 / len(vendas)}% dos vendedores atingiram a meta mensal, resultando em um total de {len(meta_atingida)} vendedores")

print("----------------------------------------------------")
print("nome dos vendedores que atingiram a meta mensal: ")
for x in range(len(vendas)):
    if vendas[x][1] > meta:
        print(vendas[x][0])

print("----------------------------------------------------")
print("nome dos vendedores que atingiram a meta mensal e seus respectivos resultados: ")
for x in range(len(vendas)):
    if vendas[x][1] > meta:
        print(f"{vendas[x][0]} ---- R$ {vendas[x][1]}")

print("----------------------------------------------------")
print("dos vendedores que não atingiram a meta mensal: ")
for x in range(len(vendas)):
    if vendas[x] not in  meta_atingida:
        print(f"{vendas[x][0]}, seja mais produtivo seu sem vergonha!")