import random

# 1) Força resultante

vetor_1 = list(map(int, input("Digite aqui as coordenadas do vetor 1: ").split()))
vetor_2 = list(map(int, input("Digite aqui as coordenadas do vetor 2: ").split()))

soma = 0

for i in range(len(vetor_1)):
    soma_coordenadas = vetor_1[i] + vetor_2[i]
    soma += soma_coordenadas

print(f"A força resultante é {soma}")

# 2) Programa que lê valores diferentes em um vetor

vetor = list(map(int, input("Digite aqui 10 valores para preencher um vetor").split()))

lista_comparacoes = []
valores_distintos = 0

for i in vetor:
    if i not in lista_comparacoes:
        lista_comparacoes.append(i)
        valores_distintos += 1

print(f"Existem {valores_distintos} valores distintos no vetor")

# 3) Encontra valor no vetor

vetor = list(map(int, input("Digite aqui os valores de um vetor").split()))
valor = int(input("Digite aqui o valor que você quer encontrar o índice"))

indices = []

for i in range(len(vetor)):
    if vetor[i] == valor:
        indices.append(i)

if indices == []:
    print(-1)
else:
    for i in indices:
        print(i) 

# 4) Dados

lancamentos = []

while len(lancamentos) != 50:
 lancamentos.append(random.randint(1, 6))

qtdd_de_6 = 0

for i in lancamentos:
    if i == 6:
        qtdd_de_6 += 1

porcentagem = qtdd_de_6 * 2

print(f"A porcentagem de ocorrências do valor 6 em 50 rolagens de dado é: {porcentagem:.2f}%")   

# Valores positivos que aparecem num vetor

vetor = list(map(int, input("Digite aqui os valores de um vetor").split()))

pos = []

for i in vetor:
    if i > 0:
        pos.append(i)

semdup = []

for i in pos:
    if i not in semdup:
        semdup.append(i)

print(f"Esse é o vetor de valores positivos que aparecem no vetor que você escreveu {semdup}")