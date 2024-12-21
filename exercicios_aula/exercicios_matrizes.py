import math

# 1) Matriz Simétrica (sua matriz transposta é ela mesma)

def verificador_simetrica(matriz):
    transposta = []
    for i in range(len(matriz[0])):
        transposta.append([0] * len(matriz))

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            transposta[j][i] = matriz[i][j]

    print("Essa é a matriz que você inseriu:")
    for i in matriz:
        print(i)
    print()       

    print("Essa é a sua matriz transposta: ")
    for i in transposta:
        print(i)
    print()

    if matriz == transposta:
        print("A sua matriz é simétrica")
    else:
        print("A sua matriz não é simétrica")             

matriz = [[2,4,3],
          [3,2,5]]

verificador_simetrica(matriz)

# 2, 3) Produto Matriz 

def produto_matriz(matriz_a, matriz_b):
    linhas_a = len(matriz_a)
    colunas_a = len(matriz_a[0])
    linhas_b = len(matriz_b)
    colunas_b = len(matriz_b[0])

    if colunas_a != linhas_b:
        print("Não é possível calcular o produto dessas matrizes")
    else:
        produto = []
        for i in range(linhas_a):
            produto.append([0] * colunas_b)

        for i in range(linhas_a):
            for j in range(colunas_b):
                for k in range(colunas_a):
                    produto[i][j] += matriz_a[i][k] * matriz_b[k][j]

        print(produto)

matriz_a = [[2,3],[1,0],[4,5]]
matriz_b = [[3,1],[2,4]]

produto_matriz(matriz_a,matriz_b)

# 4) Norma do máximo e de Frobenius

matriz = [[1,-2,3],
          [4,5,-6],
          [-7,8,9]]

maximos = []

for i in matriz:
    max = 0
    for j in i:
        if j >= 0:
            max += j
        else:
            j = j * (-1)
            max += j
    maximos.append(max)  


norma_do_maximo = 0

for i in maximos:
    if i > norma_do_maximo:
        norma_do_maximo = i

print(f"A norma do máximo da matriz é {norma_do_maximo}") 

matriz = [[1,-2,3],
          [4,5,-6]]

soma_quadrados = 0

for i in matriz:
    for j in i:
        soma_quadrados += j**2

norma_de_frobenius = math.sqrt(soma_quadrados)

print(f"A norma de Frobenius da matriz é {norma_de_frobenius:.2f}")

# 5) Submatrizes

def extrair_submatriz(matriz, i0, i1, j0, j1):
    submatriz = []

    for i in range(i0, (i1 + 1)):
        linha = []
        for j in range(j0, (j1 + 1)):
            linha.append(matriz[i][j])
        submatriz.append(linha)    

    print(submatriz)                

matriz = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
]

extrair_submatriz(matriz, 1, 2, 0, 1)

# 6) Permutação das linhas da matriz de acordo com o vetor

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

vetor = [2,0,1]

matriz_permutada = []

for i in vetor:
    matriz_permutada.append(matriz[i])

print(matriz_permutada)

# 7) Ordem crescente da soma das matrizes

matriz = [
    [7, 7, 7],
    [9, 3, 2],
    [8, 6, 9],
    [-1, 13, 6],
    [11, 6, 5],
    [1,2,3]
]

for i in range(0, len(matriz)):
    for j in range(i + 1, len(matriz)):
        if sum(matriz[i]) > sum(matriz[j]):
            matriz[i], matriz[j] = matriz[j], matriz[i]

print(matriz)

#   obs. perguntar se o professor aceita usar o método sum() 

# 8) Máximo local


# 9) Transformar matriz em vetor

def transformar_em_vetor(matriz):
    vetor = []

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            vetor.append(matriz[i][j])


    print(vetor)

matriz = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
]

transformar_em_vetor(matriz)

# 10) Palavras cruzadas
