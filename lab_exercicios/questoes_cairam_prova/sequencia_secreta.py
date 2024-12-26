# FÁCIL
# 3048

tamanho_sequencia = int(input())

sequencia = []

for i in range(tamanho_sequencia):
    numero = int(input())
    sequencia.append(numero)

numero_atual = 0

sequencia_consecutiva = []

for i in sequencia:
    if i != numero_atual:
        sequencia_consecutiva.append(i)
        numero_atual = i
    else:
        numero_atual

print(len(sequencia_consecutiva))