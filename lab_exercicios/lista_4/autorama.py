values = input().split()

numero_postos = int(values[0])
numero_carrinhos = int(values[1])
numero_leituras = int(values[2])

contador_leituras = 1

matriz = []

while contador_leituras <= numero_leituras:
    valores = input().split()
    corredor = int(valores[0])
    posto = int(valores[1])
    lista = [posto, corredor]
    matriz.append(lista)
    contador_leituras += 1

ordem = []

for i in range(1, (numero_postos + 1), 1):
    ordem.append(i)

quem_percorreu = []

for i in range(numero_carrinhos):
    quem_percorreu.append([] * numero_postos)
    
for i in range(len(matriz)):
    indice = (matriz[i][0] - 1)
    onde_passou = matriz[i][1]
    if onde_passou not in quem_percorreu[indice]:
        quem_percorreu[indice].append(onde_passou)
    elif quem_percorreu[indice] != sorted(quem_percorreu[indice]):
        quem_percorreu[indice].pop()
    elif quem_percorreu[indice] != ordem[0:len(quem_percorreu[indice])]:
        quem_percorreu[indice].pop()    


posicoes = []

for i in quem_percorreu:
    corredor = (quem_percorreu.index(i) + 1)
    quantos_postos_passou = len(i)
    lista = [quantos_postos_passou, corredor]
    posicoes.append(lista)

sorted_posicoes = sorted(posicoes, reverse=True)

final = []

for i in range(len(sorted_posicoes)):
    final.append(sorted_posicoes[i][0])

for i in final:
    print(i, end=" ", sep=" ")


# Quais controles devem ser feitos?

# Se o carrinho passar por um posto que já foi passado por ele antes, a passagem pelo posto não deverá ser contada

# Se o carrinho passar por um posto sem passar pelo posto anterior, a passagem não deverá ser contada

# Ordem cronológica para determinar o vencedor

"""
ordem = []

for i in range(1, (numero_postos + 1), 1):
    ordem.append(i)

jogador_1 = [1,2]

if jogador_1 != ordem[0:len(jogador_1)]:
    jogador_1.pop()

print(jogador_1)
"""


