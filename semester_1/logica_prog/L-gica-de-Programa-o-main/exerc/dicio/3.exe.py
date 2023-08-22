from datetime import date
dados = {}
dados["nome"] = input("qual o seu nome?")
dados["anoNasc"] = int(input("Em que ano você nasceu?"))
print("Digite o numero da sua carteira de trabalho(CTPS), se não houver, digite zero(0)")
dados["CTPS"] = int(input("CTPS:"))
dados["idade"] = date.today().year - dados["anoNasc"]

if dados["CTPS"] != 0:
    dados["anoContrato"] = int(input("Em que ano você foi contratado(a): "))
    dados["aposento"] = (30 -(date.today().year - dados["anoContrato"] )) + dados["idade"]
    dados["salario"] = float(input("Quanto é seu salário: "))
    print("="*30)
    print(f"Nome: {dados['nome']}")
    print(f"ano de nascimento: {dados['anoNasc']}")
    print(f"idade: {dados['idade']}")
    print(f"idade para se aposentar: {dados['aposento']}")
else:
    print("="*20)
    print(f"Nome: {dados['nome']}")
    print(f"ano de nascimento: {dados['anoNasc']}")
    print(f"idade: {dados['idade']}")