from functools import cmp_to_key

def ordena(pais1, pais2):
    if pais1[1] > pais2[1]:
        return -1
    elif pais1[1] < pais2[1]:
        return 1
    elif pais1[2] > pais2[2]:
        return -1
    elif pais1[2] < pais2[2]:
        return 1
    elif  pais1[3] > pais2[3]:
        return -1
    elif pais1[3] < pais2[3]:
        return 1
    elif pais1[0] < pais2[0]:
        return -1
    elif pais1[0] > pais2[0]:
        return 1
    
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

"""

Brasil 2 3 4
Noruega 8 7 5
Argentina 1 2 3
Japão 2 2 2
China 10 10 10

"""