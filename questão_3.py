def retornar_indice(palavra):
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letras_e_indice = []
    for i in range(len(letras)):
        letras_e_indice.append([i, letras[i]])
    for i in range(len(letras_e_indice)):
        for j in range(len(letras_e_indice[0])):
            if letras_e_indice[i][j]  == palavra[0]:
                return i

def cria_matriz(string):
    lista_de_palavras = string.split(" ")
    matriz = []
    for i in range(26):
        matriz.append([])
    for palavra in lista_de_palavras:
        indice = retornar_indice(palavra.lower())
        if palavra not in matriz[indice]:
            matriz[indice].append(palavra)
    return matriz

print(cria_matriz('Eu adoro correr e brincar e pular'))