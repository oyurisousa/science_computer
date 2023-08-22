n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))
if n1 < n2 < n3:
    print(n1, n2, n3)
elif n1 > n2:
    if n2 >= n3:
        print(n3, n2, n1)
    elif n3 >= n2:
        print(n2, n3, n1)
elif n2 > n1:
    if n1 >= n3:
        print(n3, n1, n2)
    elif n3 >= n1:
        print(n1, n3, n2)
elif n3 > n2:
    if n1 >= n2:
        print(n2, n1, n3)
    elif n2 >= n1:
        print(n1, n2, n3)
elif n1 == n2:
    if n1 > n3:
        print(n3, n2, n1)
    elif n1 < n3:
        print(n1, n2, n3)
else:
    print(n1, n2, n3)
