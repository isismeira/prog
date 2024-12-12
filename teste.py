# Verificador de matriz identidade

a = [[2, 1],
     [7, 4]]

b = [[4, -1],
    [-7, 2]]

#Cria o esqueleto da matriz da multiplicação e da matriz identidade

axb = [[0,0],
       [0,0]]

identidade = []

for i in range(len(a)):
     linha = [0] * len(a[0])
     identidade.append(linha)

# Atribui 1s na matriz identidade
contador = 0

for i in range(len(a)):
    identidade[i][contador] = 1
    contador += 1

# Realiza a multiplicação entre a primeira e a segunda matriz
for i in range(len(a)): # linhas de a
    for j in range(len(b[0])): # colunas de b
         for k in range(len(b)): # colunas de a / linhas de b 
              axb[i][j] += a[i][k] * b[k][j]

if axb == identidade:
     print("A segunda matriz é inversa da primeira")
else:
     print("A segunda matriz não é inversa da primeira")     