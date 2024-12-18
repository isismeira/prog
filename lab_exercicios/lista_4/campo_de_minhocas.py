# FÁCIL

values = input().split()

linhas = int(values[0])
colunas = int(values[1])

matriz = []

for i in range(linhas):
    linha = list(map(int, input().split()))
    matriz.append(linha)

direcoes_linhas = []
direcoes_colunas = []

for i in matriz:
    direcoes_linhas.append(i)

contador_coluna = 0
lista = []

while contador_coluna < len(matriz[0]):
    for i in range(len(matriz)):
        lista.append(matriz[i][contador_coluna])
    direcoes_colunas.append(lista)
    lista = []
    contador_coluna += 1

direcoes = direcoes_linhas + direcoes_colunas
somas = []

for i in direcoes:
    somas.append(sum(i))

print(max(somas))    