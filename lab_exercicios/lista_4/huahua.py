# FÁCIL

vogais = ["a", "e", "i", "o", "u"]

risada = input()

vogais_da_risada = []

for i in risada:
    if i in vogais:
        vogais_da_risada.append(i)     

vogais_da_risada_reverso = [0] * len(vogais_da_risada)

indice_vogais_da_risada = 0

for i in range(-1, ((-1 * len(vogais_da_risada)) - 1), -1):
    vogais_da_risada_reverso[i] = vogais_da_risada[indice_vogais_da_risada]
    indice_vogais_da_risada += 1

if vogais_da_risada == vogais_da_risada_reverso:
    print("S")
else:
    print("N")    