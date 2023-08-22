dicio = {}
media = 0
nome = input("qual o seu nome? ")
situacao = True
for x in range(3):
    dicio.update({f"n{x + 1}": int(input(f"nota {x + 1}: "))})

media =  (dicio["n1"]+dicio["n2"]+dicio["n3"]) / 3

if 0 > media > 10:
    print("por favor insira valores válidos(1-10)")
elif media>=7:
    situacao = "Aprovado"
elif 7 > media > 4:
    situacao = "Prova final"
elif media < 4:
    situacao = "reprovad)o"
print(f"ALuno: {nome}")
print(f"Média final: {media:.2f}")
print(f"Situação final : {situacao}")