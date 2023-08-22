"""
Escreva um programa que leia um caractere do teclado e forneça na tela uma das seguintes mensagens:
Caractere Mensagem 
A ou a Alteração 
C ou c Consulta 
E ou e Exclusão 
I ou i Inclusão 
F ou f Finalização 
Outro Opção inválida 
"""
print("caracteres válidos: A, B, E, I, F")
crt = input("Digite um caractere: ")
if crt in "Aa":
    print("Alteração")
elif crt in "Bb":
    print("Consulta")
elif crt in "Ee":
    print("Exclusção")
elif crt in "Ii":
    print("Inclusão")
elif crt in "Ff":
    print("Finalização")
else:
    print("opação inválida")
    