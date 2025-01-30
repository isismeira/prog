todas_palavras = []
preposicoes = []
palavras_filtradas = []

with open("arquivo_1.txt", "rt") as arquivo:
    texto = arquivo.read()
    texto = texto.split(" ")

    for palavra in texto:
        todas_palavras.append(palavra)

with open("prep.txt", "rt") as arquivo:
    texto = arquivo.read()
    texto = texto.split(" ")

    for palavra in texto:
        preposicoes.append(palavra)

for palavra in todas_palavras:
    if palavra not in preposicoes:
        palavras_filtradas.append(palavra) 

with open("arq_saida.txt", "wt") as arquivo:
    for palavra in palavras_filtradas:
        arquivo.write(palavra + "\n")