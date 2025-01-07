values = input().split()

jogadores = int(values[0])
rodadas = int(values[1])

lista = list(map(int, input().split()))

pontuacao = [0] * jogadores

for i in range(jogadores):
    for j in range(i, len(lista), jogadores):
        pontuacao[i] += lista[j]

maior_numero = 0

vencedor = 0

for i in range((len(pontuacao) - 1), -1, -1):
    if pontuacao[i] > maior_numero:
        vencedor = i + 1
        maior_numero = pontuacao[i]

print(vencedor)