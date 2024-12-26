from itertools import product

matriz = []

for i in range(5):
    linha = list(map(int, input().split()))
    matriz.append(linha)

conjuntos_distintos = int(input())

valores_livros = []

for i in range(len(matriz)):
    valores_livros.append(matriz[i][1:])

combinacoes = product(valores_livros[0], valores_livros[1], valores_livros[2], valores_livros[3], valores_livros[4])

print(combinacoes)

valores_dos_conjuntos = [sum(combinacao) for combinacao in combinacoes]

valores_dos_conjuntos.sort(reverse=True)

maiores_valores = valores_dos_conjuntos[:conjuntos_distintos]

soma_maiores = sum(maiores_valores)

print(soma_maiores)