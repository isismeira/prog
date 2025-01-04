import random

lista1 = ["Cachorro", "Gato", "Elefante", "Tigre", "Leao", "Cavalo", "Urso", "Raposa", "Cobra", "Lobo"]

lista2 = ["Mesa", "Cadeira", "Lampada", "Computador", "Cachorro", "Gato", "Leao", "Livro", "Relogio", "Caneta"]

intersecao = []

for i in lista1:
    if i in lista2:
        intersecao.append(i)

maior_valor = 0

for i in intersecao:
    if len(i) > maior_valor:
        maior_valor = len(i)

matriz = []

for i in range(maior_valor):
    lista = []
    for j in range(maior_valor):
        j = chr(random.randint(ord('a'),ord('z')))
        lista.append(j)
    matriz.append(lista)

preenchimento = ["diagonal", "horizontal", "vertical"]
palavras = intersecao
numeros_i = []
numeros_j = []

for i in range(maior_valor - 1):
     numeros_i.append(i)
     numeros_j.append(i)

def colocarpalavras(matriz, numeros_i, numeros_j, preenchimento, palavra):
    i =  0# random.choice(numeros_i)
    j = 0 # random.choice(numeros_j)
    direcao = "horizontal"#random.choice(preenchimento)

    if direcao == "horizontal":
        try:
            for letra in range(len(palavra)):
                matriz[i][j + letra] = palavra[letra]
            for letra in range(len(palavra)):
                numeros_i.remove(i)
                numeros_j.remove(j + letra)   
        except IndexError:
            colocarpalavras(matriz, numeros_i, numeros_j, preenchimento, palavra)

    elif direcao == "vertical":
        try:
            for letra in range(len(palavra)):
                matriz[i + letra][j] = palavra[letra]
            for letra in range(len(palavra)):
                numeros_i.remove(i + letra)
                numeros_j.remove(j) 
        except IndexError: 
            colocarpalavras(matriz, numeros_i, numeros_j, preenchimento, palavra) 

    elif direcao == "diagonal":
        try:
            for letra in range(len(palavra)):
                matriz[i + letra][j + letra] = palavra[letra]
            for letra in range(len(palavra)):
                numeros_i.remove(i + letra)
                numeros_j.remove(j + letra)
        except IndexError:
            colocarpalavras(matriz, numeros_i, numeros_j, preenchimento, palavra)                               

for palavra in intersecao:
    colocarpalavras(matriz, numeros_i, numeros_j, preenchimento, palavra)

for i in matriz:
    print(*i)