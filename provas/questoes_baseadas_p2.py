# 1) "Censurando palavras"
lista = ["Python", "diversão"]
palavras = []

with open("provas/textinho.txt", "rt", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    texto = texto.split()

    for palavra in texto:
        nova_palavra = palavra.replace(",", "").replace(".", "")
        palavras.append(nova_palavra)

with open("provas/palavras_ocultas.txt", "wt", encoding="utf-8") as arquivo:
    for palavra in palavras:
        if palavra in lista:
            arquivo.write("***" + " ")
        else:
            arquivo.write(palavra + " ")

# Frequência de Caracteres em um arquivo
matriz = []
letras = []

with open("provas/textinho.txt", "rt", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    for letra in texto:
        letras.append(letra.lower())

for letra in letras:
    tem_letra = False
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if letra == matriz[i][j]:
                tem_letra = True
                matriz[i][1] += 1
    if tem_letra == False:
        matriz.append([letra, 1])

for i in range(0, len(matriz)):
    for j in range(i + 1, len(matriz)):
        if matriz[i][1] < matriz[j][1]:
            matriz[i], matriz[j] = matriz[j], matriz[i]

with open("provas/contagem_letras.txt", "wt", encoding="utf-8") as arquivo:
    for i in range(len(matriz)):
        linha = f"{matriz[i][0]} - {matriz[i][1]} ocorrências"
        arquivo.write(linha + "\n")

# Extração de números em uma string
string = "O preço do item é 45, e o desconto é 10%. o total será 35."

string = string.split()

palavras_da_string = []

numeros = []

for palavra in string:
    nova_palavra = palavra.replace(",", "").replace(".", "").replace("%","")
    palavras_da_string.append(nova_palavra)

for palavra in palavras_da_string:
    try:
        inteiro = int(palavra)
        numeros.append(inteiro)
    except ValueError:
        pass

print(numeros)

# Matriz de frases
frases = []

string_2 = "Eu amo Python. Python é incrivel!"

string_2 = string_2.split()

frase = ""

for palavra in string_2:
    if palavra[-1] != "." and palavra[-1] != "!" and palavra[-1] != "?":
        frase += palavra + " "
    else:    
        frase += palavra + " "
        frases.append(frase)
        frase = ""

print(frases)

# Recriando o replace
def substituir(palavra, caracter):
    palavra_modificada = ""
    for letra in palavra:
        if letra != caracter:
            palavra_modificada += letra
    return palavra_modificada             

print(substituir("Olá!", "!"))

# Substituindo caracteres (sendo que tudo que estiver dentro das aspas não é removido)
def remover_pontuacao(texto, simbolos):
    novo_texto = ""
    dentro_aspas = False

    for letra in texto:
        if letra == '"':
            if dentro_aspas == False:
                novo_texto += letra
                dentro_aspas = True
            elif dentro_aspas == True:    
                novo_texto += letra
                dentro_aspas = False
        elif letra in simbolos and dentro_aspas == False:
            continue
        else:
            novo_texto += letra

    return novo_texto

print(remover_pontuacao('..%#"texto.txt",,', ['.','%', '#', ","]))            