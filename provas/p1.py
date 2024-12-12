# 1) Encontrar dígitos pares e ímpares sem usar arrays, listas ou strings
numero = int(input("Digite aqui o número: "))

pares = 0
impares = 0

while numero != 0:
    digito = numero % 10
    if digito % 2 == 0:
        pares += 1
    else:
        impares += 1
    numero = numero//10

print(f"O número de dígitos pares é {pares}")
print(f"O número de dígitos ímpares é {impares}")

# 2) Imprimir padrão conforme número de linhas e colunas

lin = int(input("Número de linhas: "))
col = int(input("Número de colunas: "))

for i in range(lin):
    for j in range(col):
        if i == 0 or i == lin - 1:
            print("x", end="") 
        elif i != 0 and (i % 2) != 0:
            if j == 0 or j == col-1:
                print("x", end="")
            else:
                if (j % 2) != 0:
                    print("o", end="")
                else:
                    print("+", end="")    
        elif i != 0 and (i % 2) == 0:
            if j == 0 or j == col-1:
                print("x", end="")
            else:
                if (j % 2) != 0:
                    print("+", end="")
                else:
                    print("o", end="")  
    print() # quebra de linha

# 3) Converter string em ascii para binário

entrada = input("Digite aqui uma string: ")

valores_strings = []

for i in entrada:
    valor = ord(i)
    binario = [0] * 8
    contador = 7
    while valor != 0:
        digito = (valor) % 2
        binario[contador] = digito 
        valor = valor//2
        contador -= 1
    string = ""
    for i in binario:
        string = string+str(i) #!!!
    valores_strings.append(string)  

resultado = ""

for i in valores_strings:
    resultado = resultado+i 
    
print(resultado)





