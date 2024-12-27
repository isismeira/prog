# 1940
# MÉDIO (mas fiz acertei de segunda)

values = input().split()
qtdd_jogadores = int(values[0])
qtdd_rodadas = int(values[1])

lista = list(map(int, input().split()))
total_pontos = []

for i in range(qtdd_jogadores):
    soma = 0
    for j in range(i, len(lista), qtdd_jogadores):
        soma += lista[j]
    total_pontos.append(soma)    

maior_valor = 0
atual_campeao = 0

for i in range(len(total_pontos) - 1, -1, -1):
    if total_pontos[i] > maior_valor:
        atual_campeao = i + 1
        maior_valor = total_pontos[i]

print(atual_campeao)
