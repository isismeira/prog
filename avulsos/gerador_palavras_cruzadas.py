import random

# Listas de palavras
palavras = ["casa", "foguete", "computador"]

# Determinar o maior comprimento de palavra
maior_palavra = 0

for i in palavras:
    if len(i) > maior_palavra:
        maior_palavra = len(i) 

# Criar a matriz de letras aleatórias
matriz = []

for i in range(maior_palavra + 5):
    linha = [0] * (maior_palavra + 5)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = chr(random.randint(ord('a'), ord('z')))    

# Função para verificar se a palavra cabe na posição 
def cabe_na_matriz_sem_conflitos(matriz, palavra, i, j, direcao):
    palavra = palavra.upper()  
    if direcao == "horizontal":
        if j + len(palavra) > len(matriz[0]):  
            return False
        for k in range(len(palavra)):  
            if matriz[i][j + k] != palavra[k] and matriz[i][j + k] != matriz[i][j + k].lower():
                return False
    elif direcao == "vertical":
        if i + len(palavra) > len(matriz):
            return False
        for k in range(len(palavra)):  
            if matriz[i + k][j] != palavra[k] and matriz[i + k][j] != matriz[i + k][j].lower():
                return False
    elif direcao == "diagonal":
        if i + len(palavra) > len(matriz) or j + len(palavra) > len(matriz[0]): 
            return False
        for k in range(len(palavra)):  
            if matriz[i + k][j + k] != palavra[k] and matriz[i + k][j + k] != matriz[i + k][j + k].lower():
                return False
    return True

# Função para inserir palavra na matriz
def inserir_palavra(matriz, palavra, i, j, direcao):
    if direcao == "horizontal":
        for k in range(len(palavra)):
            matriz[i][j + k] = palavra[k]
    elif direcao == "vertical":
        for k in range(len(palavra)):
            matriz[i + k][j] = palavra[k]
    elif direcao == "diagonal":
        for k in range(len(palavra)):
            matriz[i + k][j + k] = palavra[k]

# Função para colocar palavras aleatoriamente
def colocarpalavras(matriz, palavras):
    preenchimento = ["horizontal", "vertical", "diagonal"]
    for palavra in palavras:
        inserido = False
        while not inserido:
            # Escolher posição inicial e direção aleatórias
            i = random.randint(0, len(matriz) - 1)
            j = random.randint(0, len(matriz[0]) - 1)
            direcao = random.choice(preenchimento)

            # Verificar se a palavra cabe e inserir
            if cabe_na_matriz_sem_conflitos(matriz, palavra, i, j, direcao):
                inserir_palavra(matriz, palavra, i, j, direcao)
                inserido = True

# Inserir palavras da interseção na matriz
colocarpalavras(matriz, palavras)

# Exibir a matriz final
for linha in matriz:
    print(" ".join(linha))