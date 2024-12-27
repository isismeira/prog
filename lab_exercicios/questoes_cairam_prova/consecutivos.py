# 2415
# FÁCIL

valores = int(input())
lista = list(map(int, input().split()))

numero_atual = lista[0]
sequencias = []

sequencia = 1

for i in range(1, len(lista)):
    if lista[i] == numero_atual:
        sequencia += 1
        numero_atual = lista[i]
    else:
        numero_atual = lista[i]
        sequencias.append(sequencia)
        sequencia = 1    

# fazer o append da última sequência
sequencias.append(sequencia)

print(max(sequencias))
