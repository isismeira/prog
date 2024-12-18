# Resposta 55% certa

values = input().split()

pAB = values[0]
cAB = values[1]

pBA = values[2]
cBA = values[3]

if pAB[2:5] == ":00":
    pAB = int(pAB[0:2])
else:
    pAB = int(pAB[0:2]) + ((int(pAB[3:5]))/60)    

if cAB[2:5] == ":00":
    cAB = int(cAB[0:2])
else:
    cAB = int(cAB[0:2]) + ((int(cAB[3:5]))/60) 

if pBA[2:5] == ":00":
    pBA = int(pBA[0:2])
else:
    pBA = int(pBA[0:2]) + ((int(pBA[3:5]))/60)    

if cBA[2:5] == ":00":    
    cBA = int(cBA[0:2])
else:
    cBA = int(cBA[0:2]) + ((int(cBA[3:5]))/60)      

if (cAB - pAB) < 0 and (cBA - pBA) < 0:
    if (cAB - pAB) < (cBA - pBA):
        fusoB = (((24 - pAB) + cAB) + abs(cBA - pBA))//2
    else:
        fusoB = (((24 - pBA) + cBA) + abs(cAB - pAB))//2
        fusoB = fusoB * -1
else:           
    fusoB = ((cAB - pAB) - (cBA - pBA)) // 2

if (cAB - pAB) < 0 and (cBA - pBA) < 0:
    duracao = pAB - abs(fusoB)
    duracao = duracao * 60
else:
    duracao = (cBA - pBA) + fusoB
    duracao = duracao * 60

print(f"{duracao} {fusoB}")