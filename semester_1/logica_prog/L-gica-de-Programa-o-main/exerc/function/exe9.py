def leiaInt(question = "digite um numero: "):
    print(f"{question}",end="")
    string = input()
    num = ""
    for x in string:
        if x in ("0","1","2","3","4","5","6","7","8","9"):
            num += x
        else:
            return leiaInt("Inválido!, por favor digite somente numeros: ")
    return num

teste = leiaInt()
print(teste)