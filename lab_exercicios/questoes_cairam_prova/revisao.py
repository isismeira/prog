# 2415 
qtdd_num = int(input())

lista = list(map(int, input().split()))

numero_atual = lista[0]

repeticoes = []

sequencia = 1

for i in range(len(lista) - 1):
    if lista[i + 1] == numero_atual:
        sequencia += 1
        numero_atual = lista[i + 1]
    else:
        repeticoes.append(sequencia)
        sequencia = 1
        numero_atual = lista[i+1] 

repeticoes.append(sequencia)

print(max(repeticoes))            

# 3060 (P2)
# TEM QUE SER FEITO DESSA FORMA SE NÃO, NÃO PASSA
valor = int(input())
parcelas = int(input())

if valor % parcelas == 0:
    for i in range(parcelas):
        print(valor//parcelas)
else:
    resto = valor % parcelas
    valores = []
    for i in range(parcelas):
        valores.append(valor//parcelas)
    for i in range(resto):
        valores[i] += 1
    for i in valores:
        print(i)

# 3048 (P2)
entradas = int(input())

lista = []

for i in range(entradas):
    entrada = int(input())
    lista.append(entrada)

sequencia = 1

numero_atual = lista[0]

for i in range(len(lista) - 1):
    if lista[i + 1] != numero_atual:
        sequencia += 1
        numero_atual = lista[i+1]

print(sequencia)   

# 1940

values = input().split()

jogadores = int(values[0])
rodadas = int(values[1])

lista = list(map(int, input().split()))

pontuacao = [0] * jogadores

for i in range(jogadores):
    # obs. o pulo também é feito com a quantidade de jogadores
    for j in range(i, len(lista), jogadores):
        pontuacao[i] += lista[j]

maior_numero = 0

vencedor = 0

for i in range((len(pontuacao) - 1), -1, -1):
    if pontuacao[i] > maior_numero:
        vencedor = i + 1
        maior_numero = pontuacao[i]

print(vencedor)

# 2782
n = int(input())
lista = list(map(int, input().split()))

escadinhas = 1

if n > 1:
    diferenca = lista[1] - lista[0]

for i in range(2, n):
    # !!!
    nova_diferenca = lista[i] - lista[i -1]

    if nova_diferenca != diferenca:
        escadinhas += 1
        diferenca = nova_diferenca

print(escadinhas)

# 2391
def particoes():
    n = int(input())
    lista = list(map(int, input().split()))

    a = 1
    b = 0
    resp = 0 

    while a < n:
        if lista[a] - lista[a - 1] != lista[b + 1] - lista[b]:
            b = a
            resp += 1
            a += 1
        a += 1
    resp += 1

    print(resp)

particoes()
