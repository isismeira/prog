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
