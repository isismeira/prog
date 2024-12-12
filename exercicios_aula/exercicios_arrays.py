# 1) Soma de elementos em um array
x = [1, 2 ,3, 4, 5]

soma = 0

for i in x:
    soma += i

print(soma)    

# 2) Inserção sem insert

lista = [1,2,3,5]

def inserir(indice, valor, array):
    lista_temporaria = [0] * (len(lista)+1)
    contador = 0
    while contador < len(lista_temporaria):
        if contador < indice:
            lista_temporaria[contador] = array[contador]
            contador += 1
        elif contador == indice:
            lista_temporaria[contador] = valor
            contador += 1
        elif contador > indice:
            lista_temporaria[contador] = array[contador-1]
            contador += 1
    return lista_temporaria 

print(inserir(3, 4, lista))

# 3) Produto Escalar

vetor_a = [1, 2, 3, 4, 5]
vetor_b = [6, 7, 8, 9, 10]

contador = 0
soma = 0

while contador < len(vetor_a):
    produto = vetor_a[contador] * vetor_b[contador]
    soma += produto
    contador += 1

print(f"O produto escalar do vetor A com o vetor B é: {soma}")