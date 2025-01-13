# Pesquisa Binária
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo+ alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None

minha_lista = [2, 5, 7, 16, 19]


print(pesquisa_binaria(minha_lista, 16))
 
# Bubble Sort
lista = [3, 5, 9, 2, 9]

for i in range(0, len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j] , lista[i]

print(lista)
# Reproduzir uma matriz nova, baseada no dobro da primeiro
matriz = [[1, 2, 3],
          [3, 4, 8]]

matriz_nova = []

for i in range(2*(len(matriz))):
    linha = [0] * (2 * len(matriz[0]))
    matriz_nova.append(linha)

for i in range(len(matriz_nova)):
    for j in range(len(matriz_nova[0])):
        matriz_nova[i][j] = matriz[i//2][j//2]

for linha in matriz_nova:
    print(linha)