"""Um estacionamento cobra R$ 2,50 por cada hora ou fração de permanência de um veículo. Escreva um programa que lê os 
horários de entrada e saída de um veículo (hora e minuto) e calcule o total a ser pago. Se o veículo permanece por mais de 
quatro horas no estacionamento, ele ganha uma lavagem grátis. O seu programa deve informar ao usuário se isto ocorrer."""

print("ENTRADA")
horaEnt = float(input("hora: "))
minutosEnt = float(input("min: "))

horaEntTotal = minutosEnt / 60  + horaEnt
print("--------------------")
print("SAÍDA")
horaSai = float(input("hora: "))
minutosSai = float(input("min: "))
horaSaiTotal = minutosSai / 60 + horaSai

totalHoras = horaSaiTotal - horaEntTotal
totalPagar = totalHoras * 2.5
print("--------------------")
print(f"Total a pagar R${totalPagar}")
if totalHoras > 4.0:
    print("PARABÉNS, você ganhou uma lavagem GRÁTIS!")
else:
    print("Dica: se você premanecer por mais de 4 horas no estacionamento, ganhará uma lavagem grátis.")
