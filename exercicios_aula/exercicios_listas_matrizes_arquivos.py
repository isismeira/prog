# 1) Criando uma função que lê uma lista de palavras de um arquivo e remova todas as duplicatas

def remover_duplicatas(arq):
    with open(arq, "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()

    palavras_unicas = []

    for i in palavras:
        if i not in palavras_unicas:
            palavras_unicas.append(i)
        else:
            print(f"Removendo {i}...")    

    with open(arq, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(palavras_unicas)


arq = "exercicios_aula/palavras.txt"

remover_duplicatas(arq)

# 2) Sorting Algorithms em arquivos

#   Bubble Sort
def bubble_sort(arq):
    with open(arq, "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()
     
    for i in range(0, len(palavras)):
        for j in range(i + 1, len(palavras)):
            if palavras[i] > palavras[j]:
                palavras[i], palavras[j] = palavras[j], palavras[i]

    with open(arq, "w", encoding="utf-8") as arquivo:
     arquivo.writelines(palavras)               

arq = "palavras.txt"
bubble_sort(arq)

#    Insertion Sort

def insertion_sort(arq):
    with open(arq, "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()
    
    for i in range(1, len(palavras)):
        j = i
        while palavras[j-1] > palavras[j] and j > 0:
            palavras[j - 1], palavras[j] = palavras[j], palavras[j-1]
            j -= 1

    with open(arq, "w", encoding="utf-8") as arquivo:
       arquivo.writelines(palavras)

arq = "palavras.txt"
insertion_sort(arq)

#    Selection Sort

def selection_sort(arq):
    with open(arq, "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()

    for i in range(0, len(palavras) - 1):
        indice_minimo_atual = i
        for j in range(i+1, len(palavras)):
            if palavras[j] < palavras[indice_minimo_atual]:
                indice_minimo_atual = j

        palavras[i], palavras[indice_minimo_atual] = palavras[indice_minimo_atual], palavras[i]

    with open(arq, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(palavras)

arq = "palavras.txt"
selection_sort(arq)

# obs. o gerador de caça palavras está na pasta "avulsos"

# 3) Interseção das listas
lista1 = ["Cachorro", "Gato", "Elefante", "Tigre", "Leao", "Cavalo", "Urso", "Raposa", "Cobra", "Lobo"]
lista2 = ["Mesa", "Cadeira", "Lampada", "Computador", "Cachorro", "Gato", "Leao", "Livro", "Relogio", "Caneta"]

intersecao = []

for palavra in lista1:
    if palavra in lista2:
        intersecao.append(palavra)

# 4) União das listas
uniao = []

for palavra in lista1:
    uniao.append(palavra)
for palavra in lista2:
    if palavra not in uniao:
        uniao.append(palavra)


# 5) Diferença das listas

diferenca = []

for palavra in lista1:
    if palavra not in intersecao:
        diferenca.append(palavra)

print(intersecao)
print(uniao)
print(diferenca)

# 6) Exercício feito na pasta "avulsos"