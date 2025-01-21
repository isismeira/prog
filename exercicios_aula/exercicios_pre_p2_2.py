# 1) Insere uma linha de zeros numa posição determinada
def insere_linhas(matriz, indice):
    matriz_nova = []
    linha = [0] * len(matriz[0])

    for i in range(len(matriz) + 1):
        if i < indice:
            matriz_nova.append(matriz[i])
        elif i == indice:
            matriz_nova.append(linha)
        else:
            matriz_nova.append(matriz[i-1])
    return matriz_nova

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(insere_linhas(matriz, 1))

# 2) Ordena a matriz baseado na soma de cada linha
def ordenar_matriz(matriz):
    
    nova_matriz = []
    indices_e_soma = []

    for i in range(len(matriz)):
        soma_linha = 0
        for j in range(len(matriz[0])):
            soma_linha += matriz[i][j]
        lista = [i, soma_linha]
        indices_e_soma.append(lista)

    for i in range(0, len(indices_e_soma)):
        for j in range(i+1, len(indices_e_soma)):
            if indices_e_soma[i][1] > indices_e_soma[j][1]:
                indices_e_soma[i], indices_e_soma[j] = indices_e_soma[j], indices_e_soma[i]

    for i in range(len(indices_e_soma)):
        nova_matriz.append(matriz[indices_e_soma[i][0]])

    return nova_matriz  

matriz = [
    [7, 7, 7],
    [9, 3, 2],
    [8, 6, 9],
    [-1, 13, 6],
    [11, 6, 5],
    [1,2,3]
]              

print(ordenar_matriz(matriz))

# 3) Gerar arquivo com a interseção das palavras
palavras_1 = []
palavras_2 = []
intersecao = []

with open("arquivo_1.txt", "rt", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    texto = texto.split()
    for palavra in texto:
        palavras_1.append(palavra)

with open("arquivo_2.txt", "rt", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    texto = texto.split()
    for palavra in texto:
        palavras_2.append(palavra)

for palavra in palavras_1:
    if (palavra in palavras_2) and (palavra not in intersecao):
        intersecao.append(palavra)

with open("arquivo_saida.txt", "wt", encoding="utf-8") as arquivo:
    for palavra in intersecao:
        arquivo.write(palavra + "\n")   