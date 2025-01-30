linhas_matriz = []
matriz = []

with open("caca_palavras.txt", "rt", encoding="utf-8") as arquivo:
    texto = arquivo.readlines()
    for i in range(1, len(texto)):
        linhas_matriz.append(texto[i])

for linha in linhas_matriz:
    linha_tratada = linha.replace("\n", "")
    linha_tratada = linha_tratada.split(" ")
    matriz.append(linha_tratada)

print(matriz)            