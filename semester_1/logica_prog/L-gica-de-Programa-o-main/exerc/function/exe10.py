def notas(*notas,sit= False):
    notas = list(notas)
    raioX = {
        'quant_notas' : len(notas),
        'maior_nota' :  max(notas),
        'menor_nota' : min(notas),
        'media' : (sum(notas) / len(notas)),        
    }
    if sit == True:
        situacao = 0
        if raioX['media'] < 4:
            situacao = "Reprovado por nota(RN)"
        elif raioX['media'] >= 7 :
            situacao = "aprovado"
        else:
            situacao = "Prova final(PF)" 
        raioX['situação']  = situacao
    return raioX



print(notas(8,7,5,sit = True))