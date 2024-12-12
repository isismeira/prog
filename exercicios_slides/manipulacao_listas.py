import random
# 1) Dados

lancamentos = []

while len(lancamentos) != 100:
 lancamentos.append(random.randint(1, 6))

qtdd_de_1 = 0
qtdd_de_2 = 0
qtdd_de_3 = 0
qtdd_de_4 = 0
qtdd_de_5 = 0
qtdd_de_6 = 0

for i in lancamentos:
    if i == 1:
        qtdd_de_1 += 1
    elif i == 2:
        qtdd_de_2 += 1
    elif i == 3:
        qtdd_de_3 += 1
    elif i == 4:
        qtdd_de_4 += 1   
    elif i == 5:
        qtdd_de_5 += 1   
    elif i == 6:
        qtdd_de_6 += 1                                         

ocorrencias = [qtdd_de_1, qtdd_de_2, qtdd_de_3, qtdd_de_4, qtdd_de_5, qtdd_de_6]

print(ocorrencias)

# 2) Valor próximo da média

notas = list(map(float, input("Digite aqui as notas dos alunos: ").split()))

soma_notas = 0

for i in notas:
    soma_notas += i

media = soma_notas/len(notas)

diferencas_notas = []

for i in notas:
    diferenca = abs(media - i)
    diferencas_notas.append(diferenca)

print(f"Média: {media}")
print(f"Valor mais próximo da média: {notas[diferencas_notas.index(min(diferencas_notas))]}")

# 3) Listas Intercaladas

lista_1 = list(map(int, input("Digite aqui os valores da lista um: ").split()))
lista_2 = list(map(int, input("Digite aqui os valores da lista dois: ").split()))

lista_intercalada = [0] * (len(lista_1) + len(lista_2))

for j in range(len(lista_1)):
    for i in range(0, len(lista_intercalada), 2):
        lista_intercalada[i] = lista_1[j]

for j in range(len(lista_2)):
    for i in range(1, len(lista_intercalada), 2):
        lista_intercalada[i] = lista_2[j]        

print(lista_intercalada)