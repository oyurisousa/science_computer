n1 = int(input("Digite um número: "))
n2 = int(input("você quer dividir por quanto?(diferente de 0) "))

res = 0

if n2 == 0:
    print(ZeroDivisionError("Matematicamente não existe divisão por zero, tente novamente"))
else:
    res = n1/n2
    print(f"{n1} / {n2} = {res}")
