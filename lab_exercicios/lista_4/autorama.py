values = input().split()

numero_postos = int(values[0])
numero_carrinhos = int(values[1])
numero_leituras = int(values[2])

contador_leituras = 1

matriz = []

while contador_leituras <= numero_leituras:
    valores = input().split()
    corredor = valores[0]
    posto = valores[1]
    lista = [valores[0], valores[1]]
    lista.append(matriz)

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

        