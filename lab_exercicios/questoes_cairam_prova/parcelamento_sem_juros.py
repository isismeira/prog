# FÁCIL
# 3060

valor = int(input())
parcelas = int(input())

if valor % parcelas == 0:
    for i in range(parcelas):
        print(valor//parcelas)
else:
    resto = valor % parcelas
    valores = []
    for i in range(parcelas):
        valores.append(valor//parcelas)
    for i in range(resto):
        valores[i] += 1
    for i in valores:
        print(i)               