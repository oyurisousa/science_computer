#Carlos Yuri Brito de Sousa, bloco 1

from datetime import timedelta

def Tempo(): # função que executará tudo
    quant_teste = int(input()) #recebe a quantidade de testes desejáveis

    #verificar se a quantidade de testes está nos padrões(1=<x<=100)
    if quant_teste < 1 or quant_teste > 100:
        return
    testes = {} 
    # associar cada teste a uma chave dentro do dict testes, separando os dois horarios em uma lista 
    for x in range(quant_teste):
        testes[f'teste_{x+1}'] = input().split(" ")

    parts = {}
    for x in range(quant_teste): # separar hora,minuto e segundo
        parts[f"teste_{x+1}"] = []
        parts[f"teste_{x+1}"].append(testes[f'teste_{x+1}'][0])
        parts[f"teste_{x+1}"][0] = parts[f"teste_{x+1}"][0].split(",")
        parts[f"teste_{x+1}"].append(testes[f'teste_{x+1}'][1])
        parts[f"teste_{x+1}"][1] = parts[f"teste_{x+1}"][1].split(",")
        parts[f"teste_{x+1}"][0][0] = parts[f"teste_{x+1}"][0][0].split(":") 
        parts[f"teste_{x+1}"][1][0] = parts[f"teste_{x+1}"][1][0].split(":") 

    hms = {} #hms -> hora,minuto,segundo
    for x in range(quant_teste): #criar uma chave para cada h,m e s
        hms[f'teste_{x+1}'] = [{
            'hora':int(parts[f"teste_{x+1}"][0][0][0]),
            'min' : int(parts[f"teste_{x+1}"][0][0][1]),
            'sec' : int(parts[f"teste_{x+1}"][0][0][2])
        },
        {
            'hora':int(parts[f"teste_{x+1}"][1][0][0]),
            'min' : int(parts[f"teste_{x+1}"][1][0][1]),
            'sec' : int(parts[f"teste_{x+1}"][1][0][2])
        }]

    teste_sec={}
    for x in range(quant_teste): #realizar todas os possiveis casos de horarios
        if parts[f"teste_{x+1}"][0][1].lower() == "am" and parts[f"teste_{x+1}"][1][1].lower() == "am":
            if hms[f'teste_{x+1}'][0]['hora'] > hms[f'teste_{x+1}'][1]['hora']:
                hms[f'teste_{x+1}'][1]['hora'] += 12
            elif hms[f'teste_{x+1}'][0]['hora'] == hms[f'teste_{x+1}'][1]['hora']: 
                if hms[f'teste_{x+1}'][0]['min'] > hms[f'teste_{x+1}'][1]['min']:
                    hms[f'teste_{x+1}'][1]['hora'] += 24 
                    if hms[f'teste_{x+1}'][0]['sec'] > hms[f'teste_{x+1}'][1]['sec']:
                        hms[f'teste_{x+1}'][1]['hora'] += 24 
        elif parts[f"teste_{x+1}"][0][1].lower() == "pm" and parts[f"teste_{x+1}"][1][1].lower() == "pm":
            if hms[f'teste_{x+1}'][0]['hora'] > hms[f'teste_{x+1}'][1]['hora']:
                hms[f'teste_{x+1}'][1]['hora'] += 24
            
        elif parts[f"teste_{x+1}"][0][1].lower() == "am" and parts[f"teste_{x+1}"][1][1].lower() == "pm":
            if parts[f"teste_{x+1}"][0][0] == ['12','00','00'] :
                hms[f'teste_{x+1}'][1]['hora'] += 24
            elif hms[f'teste_{x+1}'][1]['hora'] == 12:
                hms[f'teste_{x+1}'][1]['hora']  = hms[f'teste_{x+1}'][1]['hora'] 
            elif hms[f'teste_{x+1}'][0]['hora'] > hms[f'teste_{x+1}'][1]['hora']:
                hms[f'teste_{x+1}'][1]['hora'] += 12
            else:
                hms[f'teste_{x+1}'][1]['hora'] += 12
        elif parts[f"teste_{x+1}"][0][1].lower() == "pm" and parts[f"teste_{x+1}"][1][1].lower() == "am":
            hms[f'teste_{x+1}'][1]['hora'] += 12 
           
        date1 = timedelta(hours=hms[f'teste_{x+1}'][0]['hora'],minutes=hms[f'teste_{x+1}'][0]['min'],seconds =hms[f'teste_{x+1}'][0]['sec'])
        date2 = timedelta(hours=hms[f'teste_{x+1}'][1]['hora'],minutes=hms[f'teste_{x+1}'][1]['min'],seconds=hms[f'teste_{x+1}'][1]['sec'])
        teste_sec[f'teste_{x+1}'] = int((date2 - date1).total_seconds())
    print()

    for x in range(quant_teste): #imprimir os segundo de cada teste
        print(teste_sec[f'teste_{x+1}'])
        
Tempo()

"""
01:04:53,am 01:05:00,am
12:00:00,am 01:00:00,am
12:00:00,am 01:00:00,pm 
10:00:00,am 01:00:00,pm 
05:00:00,pm 04:00:00,pm 
07:00:00,pm 07:00:00,am 
03:25:46,am 03:25:46,am

04:50:13,am 09:59:12,pm
10:44:54,am 06:09:46,am
11:02:08,am 08:05:18,pm
03:25:17,am 03:24:54,am
01:59:13,am 12:37:18,pm
"""