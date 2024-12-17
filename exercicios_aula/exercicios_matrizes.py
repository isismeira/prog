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

# OBS ACHAR OS ELEMENTOS DA MATRIZ NO VETOR E VICE VERSA