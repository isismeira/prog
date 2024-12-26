# DIFÍCIL
# Exige o uso de uma biblioteca

from functools import cmp_to_key

def ordena(pais1, pais2):
    # comparação das medalhas de ouro
    if pais1[1] > pais2[1]:
        return -1
    elif pais1[1] < pais2[1]:
        return 1
    
    # comparação das medalhas de prata
    elif pais1[2] > pais2[2]:
        return -1
    elif pais1[2] < pais2[2]:
        return 1
    
    # comparação medalhas bronze
    elif  pais1[3] > pais2[3]:
        return -1
    elif pais1[3] < pais2[3]:
        return 1
    
    # comparação alfabética
    elif pais1[0] < pais2[0]:
        return -1
    elif pais1[0] > pais2[0]:
        return 1
    
    # em caso de empate total...
    return 0

paises = int(input())

matriz = []

for i in range(paises):
    values = input().split()
    pais = values[0]
    ouro = int(values[1])
    prata = int(values[2])
    bronze = int(values[3])
    matriz.append([pais, ouro, prata, bronze])

matriz.sort(key=cmp_to_key(ordena))

for i in matriz:
    print(*i)
