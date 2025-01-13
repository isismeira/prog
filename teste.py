with open("texto.txt", "rt", encoding="utf-8") as arquivo:
    texto = arquivo.readlines()

matriz = []

for i in texto:
    linha = i.split(',')
    for j in linha:
        
    matriz.append(linha)    

print(matriz)           