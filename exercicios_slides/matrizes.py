# 1) Linha de maior soma de uma matriz 3x3

matriz = []

while len(matriz) != 3:
    linha = list(map(int, input("Digites os três valores de uma linha: ").split()))
    matriz.append(linha)

somas = []

for i in matriz:
    soma = 0
    for j in i:
        soma += j
    somas.append(soma)

print(f"A linha de maior soma é a linha {somas.index(max(somas))+1}")        

# 2) Soma de matrizes 2x2

def soma_matrizes():

    matriz_1 = []
    matriz_2 = []

    while len(matriz_1) != 2:
        linha = list(map(int, input("Digites os dois valores de uma linha da matriz 1: ").split()))
        matriz_1.append(linha)

    while len(matriz_2) != 2:
        linha = list(map(int, input("Digites os dois valores de uma linha da matriz 2: ").split()))
        matriz_2.append(linha)    

    matriz_3 = []

    for i in range(len(matriz_1[0])):
        linha = [0] * (len(matriz_1[0]))
        matriz_3.append(linha)


    for i in range(len(matriz_1)): # linhas
            for j in range(len(matriz_1[0])): # colunas
                matriz_3[i][j] = matriz_1[i][j] + matriz_2[i][j]

    print(matriz_3)            
                
soma_matrizes()

# 3) Multiplicao de matrizes

def multiplicar_matrizes(matriz_a, matriz_b):
    #Dimensões das matrizes
    linhas_a = len(matriz_a)
    colunas_a = len(matriz_a[0]) # também é o valor de linhas da matriz b
    colunas_b = len(matriz_b[0])

    #Criando uma matriz resultado com vários zeros
    matriz_resultado = []
    for i in range(linhas_a):
        linha = [0] * colunas_b
        matriz_resultado.append(linha)

    # Multiplicação
    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return matriz_resultado            


matriz_a = [[1,2],
            [3,4],
            [5,6]]

matriz_b = [[7,8,9],
            [10,11,12]]

matrizes = multiplicar_matrizes(matriz_a, matriz_b)
print(matrizes)


# 4) Matriz com linha de maior soma 
matriz = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]

somas = []
soma = 0

for i in matriz:
    for j in i:
        soma += j
    somas.append(soma)
    soma = 0

print(f"A linha de maior soma é a linha {somas.index(max(somas)) + 1}")
print(f"A sua soma resulta em {max(somas)}")

# 5) Matriz Transposta

matriz = [
   [1,2,3],
   [4,5,6],
   [7,8,9],
   [10,11,12]
]

matriz_t = []

for j in matriz[0]:
    linha = [0] * len(matriz)
    matriz_t.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz_t[j][i] = matriz[i][j]

print(matriz_t)

# 6) Corrida de Kart

matriz = [["Carlos", 6, 9, 9 ],
          ["José", 4, 5, 6],
          ["João", 10, 8, 9]]

soma = 0

tempos_corredores = []

for i in range(len(matriz)):
    for j in range(1, len(matriz[i])):
        soma += matriz[i][j]
    tempos_corredores.append(soma)
    soma = 0

corrida = []

for i in tempos_corredores:
    linha = [matriz[tempos_corredores.index(i)][0], i]
    corrida.append(linha)

ranking = sorted(corrida, key=lambda x: x[1])

print("---Ordem de Chegada---")
for i in range(len(ranking)):
        print(f"{i + 1} Lugar: {ranking[i][0]} (com {ranking[i][1]}s para terminar a prova)")
print()        

matriz_tempos = []

for i in range(len(matriz)):
    linha = []
    for j in range(1, len(matriz[i])):
        linha.append(matriz[i][j])
    matriz_tempos.append(linha)
    linha = []

menor_valor = matriz_tempos[0][0]

for i in range(len(matriz_tempos)):
     for j in range(len(matriz_tempos[0])):
          if matriz_tempos[i][j] < menor_valor:
               menor_valor = matriz_tempos[i][j]
               indice_linha = i

print("---Volta mais rápida---")
print(f"A volta mais rápida foi feita pelo jogador {matriz[indice_linha][0]}, e o seu tempo foi de {menor_valor}s")

# 7) Lendo o maior e menor elemento da matriz

matriz = [
    [1, 2, 8],
    [9, 3, 2],
    [-1, 13, 6],
    [7, 7, 7],
    [11, 6, 5],
    [8, 6, 9]
]

menor_valor = matriz[0][0]
maior_valor = matriz[0][0]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] < menor_valor:
            menor_valor = matriz[i][j]
            linha_menor_valor = i
            coluna_menor_valor = j

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            linha_maior_valor = i
            coluna_maior_valor = j

print(f"O maior elemento da matriz é {maior_valor}, ele está na linha{(linha_maior_valor) + 1} e na coluna {(coluna_maior_valor) + 1}")
print()
print(f"O menor elemento da matriz é {menor_valor}, ele está na linha{(linha_menor_valor) + 1} e na coluna {(coluna_menor_valor) + 1}")

# 8) Verifica se é matriz inversa


a = [[2, 1],
     [7, 4]]

b = [[4, -1],
    [-7, 2]]

#    Cria o esqueleto da matriz da multiplicação e da matriz identidade

axb = [[0,0],
       [0,0]]

identidade = []

for i in range(len(a)):
     linha = [0] * len(a[0])
     identidade.append(linha)

#      Atribui 1s na matriz identidade
contador = 0

for i in range(len(a)):
    identidade[i][contador] = 1
    contador += 1

#      Realiza a multiplicação entre a primeira e a segunda matriz
for i in range(len(a)): # linhas de a
    for j in range(len(b[0])): # colunas de b
         for k in range(len(b)): # colunas de a / linhas de b 
              axb[i][j] += a[i][k] * b[k][j]

if axb == identidade:
     print("A segunda matriz é inversa da primeira")
else:
     print("A segunda matriz não é inversa da primeira")

# 9)          