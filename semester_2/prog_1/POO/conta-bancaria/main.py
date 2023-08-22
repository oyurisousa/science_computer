from conta import Conta
from agencia import Agencia
from banco import Banco
import os

def menu_principal():
    print("""
    ############## MENU PRINCIPAL ##############
    
    1.Criar conta
    2.Entrar
    3.Ver contas
    4.Cadastrar agencia
    0.Sair 
    """)

    acao = input('O que você deseja fazer ->')
    limpa()
    if acao == '0':
        print("você saiu!")
        return
    elif acao == '1':
        
        print("=============== CRIANDO CONTA ===============")
        try:
            nome = input("Nome: ")
            cpf = input('CPF: ')
            cidade = input("cidade:")
            endereco = input("endereco: ")
            uf = input("uf: ")
            saldoI = float(input("Saldo Inicial: "))
            
        except:
            limpa()
            print("Por favaor digite apenas numeros!")
            return menu_principal()
        else:
            criar_conta(nome, cpf, cidade, endereco,uf,saldoI)
    elif acao == '2':
        try:
            num = int(input("numero da sua conta: "))
        except:
            limpa()
            print("conta inválida!")
            return menu_principal()
        else:
            limpa()
            login(num)
    elif acao == '3':
        if len(Agencia.contas) > 0:
            for i,x in enumerate(Agencia.contas):
                print(f"{i}. {x.nome} {x.numero}")
        else:
            print("NÂO EXISTEM CONTAS CADASTRADAS NESSA AGENCIA")
        
        return menu_principal()
    elif acao == '4':
        try:
            numero = int(input("numero: "))
            cidade = input("cidade: ")
            endereco = input("endereco: ")
            uf = input("UF: ")
        except:
            print("o numero da agência deve ser um numero vaĺido!")
        
        banco_central.agencias.append(Agencia(numero,cidade,endereco,uf))
        with open('data/agencias.txt','a') as file:
            file.write(f"{numero}{cidade}{endereco}{uf}\n")
        print("Agência cadastrada com sucesso!")
        menu_principal()

    else:
        print('opção invalida')
        return menu_principal()

def criar_conta(nome, cpf,cidade, endereco,uf,saldoI = 0):
    print(f"""
        ESCOLHA SUA AGÊNCIA

    """)
    for i,x in enumerate(banco_central.agencias):
        print(f"{i+1}. {x.numero} - {x.cidade}-{x.uf}")
    try:
        acao = int(input("-> "))
    except:
        print("Numero inválido! ")
        return criar_conta(nome,cpf,cidade,endereco,uf,saldoI)
    x = Conta(nome,cpf,cidade,endereco,uf,banco_central.agencias[acao-1].numero,saldoI)
    Agencia.contas.append(x)
    limpa()
    print(f"Parabéns {x.nome}, sua conta foi criada com sucesso!")
    print(f"O número da sua conta é {x.numero}")
    return menu_conta(x)

def login(conta):
    try:
        if Conta.existe_conta(conta):
            menu_conta(Conta.existe_conta(conta))
        else:
            print("Essa conta não existe!")
            menu_principal()
    except:
        limpa()
        print("Valores inválidos!")
        print("por favor digite apenas numeros.")
        return menu_principal()

def menu_conta(x):
    print(f"""
    =============== MENU CONTA ===============
    titular: {x.nome}  conta: {x.numero}
    ------------------------------------------
    1.ver saldo
    2.depositar
    3.sacar
    4.transferir
    5.extrato
    0.sair
    
    """)
    acao = input("O que você deseja fazer -> ")
    limpa()
    if acao == '0':
        print("Você foi deslogado!")
        return menu_principal()
    elif acao == '1':
        limpa()
        print(f"SALDO: {x.saldo}")
        return menu_conta(x)
    elif acao == '2': 
        try:
            valor = int(input("Valor: "))
        except:
            limpa()
            print("valor inválido!")
            return menu_conta(x)
        else:
            limpa()
            x.depositar(valor)
            return menu_conta(x)
    elif acao == '3':
        try:
            valor = int(input("Valor: "))
        except:
            limpa()
            print("valor inválido!")
            return menu_conta(x)
        else:
            limpa()
            x.sacar(valor)
            return menu_conta(x)
    elif acao == '4':
        try:
            contaD = int(input(f'Conta de destino-> '))
            valor = int(input("Valor: "))
        except:
            print("valor inválido!")
            return menu_conta(x)
        else:
            x.transferir(contaD,valor)
            return menu_conta(x)
    elif acao == '5':
        print(f"    ============== EXTRATO ==============")
        x.extrato()
        return menu_conta(x)
    else:
        limpa()
        print("Opção invalida!")
        return menu_conta(x)

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')
    
if __name__ == "__main__":
    banco_central = Banco("Python Brasil",1234567890)

    with open("data/agencias.txt",'r') as file:
        for x in file:
            lista = x.strip().split()
            banco_central.agencias.append(Agencia(lista[0],lista[1],' '.join(lista[2:-1]),lista[-1]))      
    
    menu_principal()

   