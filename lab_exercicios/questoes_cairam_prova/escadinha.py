# 2782
# DIFÍCIL
# Estudar a lógica

n = int(input())
sequencia = list(map(int, input.split()))

escadinhas = 1 # toda sequência terá pelo menos uma escadinha

# se houver mais de um valor na sequencia...
if n > 1:
    # ... a sequencia inicial será entre o segundo e primeiro valor
    diferenca = sequencia[1] - sequencia[0]

# para indices entre 2 e o valor de numeros na sequencia
for i in range(2, n):
    # calculará a nova diferenca entre os proximos numeros da sequencia inicial
    nova_diferenca = sequencia[i] - sequencia[i-1]
    # se a diferença nao for a mesma...
    if nova_diferenca != diferenca:
        # significa que uma nova escadinha existe
        escadinhas += 1
        # atualiza-se a nova diferenca a ser comparada
        diferenca = nova_diferenca

print(escadinhas)

