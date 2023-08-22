"""
Dados os números reais a, b e c determine as raízes da equação de segundo grau ax2 + bx + c = 0 indicando se as raízes
são reais ou complexas. Considere também o caso em que a = 0
"""
a = float(input("Valor do a: "))
b = float(input("Valor do b: "))
c = float(input("Valor do c: "))
delta = float((b*b)-(4*a*c))

if delta < 0:
    print("naõ exite raiz real, as raízes são complexas")
elif b == c == 0:
    print("ambas as raizes são nulas(0)")
elif c == 0:
    x1 = 0
    x2 = -(b) / (a)
    print(x1,x2)
elif b == 0:
    x1 = (-(c)/(a))**0.5
    x2 = -(x1)
    print(x1, x2, "b = 0")
elif b != 0 and c != 0:
    x1 = ((-(b)) + (delta ** 0.5)) / (2*(a))
    x2 = ((-(b)) - (delta ** 0.5)) / (2*(a))
    print(x1, x2)
else:
    print("Valores inválido")

