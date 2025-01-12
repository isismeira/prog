with open("avulsos/feudalismo.txt", "rt", encoding="utf-8") as arquivo:
    texto = arquivo.read()

texto = texto.split()

lista = []

for palavra in texto:
    palavra = palavra.replace(".","").replace(",","")
    lista.append(palavra)

contador = {}

for palavra in lista:
    palavra = palavra.lower()
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

print(contador)