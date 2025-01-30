# Insertion Sort
for i in range(1, len(array)):
    j = i
    while array[j - 1] > array[j] and j>0:
        array[j-1], array[j] = array[j], array[j-1]
        j -= 1

# Selection Sort
for i in range(0, len(array) - 1):
    indice_min = i
    for j in range(i+1, len(array)):
        if array[j] < array[indice_min]:
            indice_min = j
    array[i], array[indice_min] = array[indice_min], array[i]    

# Pesquisa Binária
def pesquisa_binaria(lista, item):
    alto = len(lista) - 1
    baixo = 0

    while baixo <= alto:
        meio = (alto + baixo)//2
        chute = lista[meio]

    if chute == item:
        return meio
    elif chute > item:
        alto = meio - 1
    else:
        baixo = meio + 1

    return None    

# Produto de Matrizes
def produto_matrizes(matriz_a, matriz_b):
    linhas_a = len(matriz_a)
    colunas_a = len(matriz_a[0])
    linhas_b = len(matriz_b)
    colunas_b = len(matriz_b[0])

    if colunas_a != linhas_b:
        print('Não é possível calcular')
    else:
        matriz_nova = []
        for i in range(linhas_a):
            matriz_nova.append([0] * colunas_b)
        for i in range(linhas_a):
            for j in range(colunas_b):
                for k in range(linhas_b):
                    matriz_nova[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return matriz_nova                

# Números Primos
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, n + 1):
    print(i, end=" ")
    
# MDC e MMC
def calcular_mdc(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def calcular_mmc(a,b):
    mdc = calcular_mdc(a,b)
    return abs(a * b)//mdc
    