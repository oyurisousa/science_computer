
def fatorial(number,show = True):
    print(f"fat({number}) = ", end="")
    if number != 0:
        fatorial = number
        print(f"{number}*",end="")
        number -= 1
        for x in range(number):
            fatorial = fatorial*number
            print(f"{number}*",end="")
            number -= 1
            if number == 1:
                print(f"{number} = {fatorial}")
    else:
        print(1)

fatorial(6)