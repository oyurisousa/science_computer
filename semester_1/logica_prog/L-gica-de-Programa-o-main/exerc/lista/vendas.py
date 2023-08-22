meses = ['JAN','FEV','MAR', 'ABR', 'MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
vendas_1sem = [25000,29000,22200,17750,15870,19960]
vendas_2sem = [9850,20120,17540,15555,49051,19650]
vendas_ano = vendas_1sem + vendas_2sem
maior = vendas_ano[0]
menor = vendas_ano[0]
faturamento_anual = 0
i = 0
j = 0
for x in range(12):
    if vendas_ano[x] > maior:
        maior = vendas_ano[x]
        i = x 
    elif vendas_ano[x] < menor:
        menor = vendas_ano[x]
        j = x
print(f"o mês com maior faturamento foi {meses[i]} com {maior}")
print(f"o mês com menor faturamento foi {meses[j]} com {menor}")

for x in range(len(vendas_ano)):
    faturamento_anual += vendas_ano[x]
print(f"O faturamento anual foi de {faturamento_anual}")

porcen = (100*maior)/faturamento_anual
print(porcen)
