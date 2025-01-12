with open('avulsos/saida.txt', "rt", encoding="utf-8") as arquivo:
    texto = arquivo.readlines()

matriz = []

for linha in texto:
    lista = linha.strip().split(",")
    matriz.append(lista)

print(matriz)    