# FÁCIL
values = input().split()

n_carros = int(values[0])
n_voltas = int(values[1])

matriz = []

for i in range(n_carros):
    dados = list(map(int, input().split()))
    matriz.append(dados)

tempo_corredores = []

for i in range(len(matriz)):
    tempo = sum(matriz[i])
    indice_corredor = i + 1
    lista = [tempo, indice_corredor]
    tempo_corredores.append(lista)

# Basta utilizar o sort, que utilizará como primeira coluna como primeiro critério de organização e depois a segunda coluna para critério de desempate
tempo_corredores.sort()

for i in range(3):
    print(tempo_corredores[i][1])