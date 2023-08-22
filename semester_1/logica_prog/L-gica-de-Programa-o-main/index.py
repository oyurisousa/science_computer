vendedores = ["João", "Maria", "José", "Pedro"]
vendas = [1500.0, 2000.0, 1000.0, 750.0]
meta = 1000.0

# Mostra quantos vendedores atingiram a meta mensal e a porcentagem desse total
num_vendedores_atingiram_meta = 0
for i in range(len(vendedores)):
  if vendas[i] >= meta:
    num_vendedores_atingiram_meta += 1

porcentagem_atingiram_meta = (num_vendedores_atingiram_meta / len(vendedores)) * 100
print(str(num_vendedores_atingiram_meta) + " vendedores atingiram a meta mensal (" + str(porcentagem_atingiram_meta) + "%)")

# Mostra o nome de todos os vendedores que atingiram a meta
print("Vendedores que atingiram a meta:")
for i in range(len(vendedores)):
  if vendas[i] >= meta:
    print(vendedores[i])

# Mostra o nome de todos os vendedores que atingiram a meta e seus valores atingidos
print("Vendedores que atingiram a meta e seus valores atingidos:")
for i in range(len(vendedores)):
  if vendas[i] >= meta:
    print(vendedores[i] + ": " + str(vendas[i]))

# Mostra a mensagem "Fulano, seja mais produtivo!" para os vendedores que não atingiram a meta mensal
print("Vendedores que não atingiram a meta:")
for i in range(len(vendedores)):
  if vendas[i] < meta:
    print(vendedores[i] + ", seja mais produtivo!")