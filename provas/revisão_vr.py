# Desenhando padrão
lin = int(input("Digite aqui o número de linhas: "))
col = int(input("Digite aqui o número de colunas: "))

for i in range(lin):
    for j in range(col):
        if i == 0 or i == lin - 1:
            print("x", end="")
        elif i != 0 and i % 2 != 0:
            if j == 0 or j == col - 1:
                print("x", end="")
            elif j % 2 == 0:
                print("+", end="")
            else:
                print("o", end="")
        elif i != 0 and i % 2 == 0:
            if j == 0 or j == col - 1:
                print("x", end="")
            elif j % 2 == 0:
                print("o", end="")
            else:
                print("+", end="")
    print()

# Invertendo o número (sem string)
numero = 12648
inverso = 0

while numero != 0:
    ultimo_digito = numero%10
    inverso = inverso * 10 + ultimo_digito
    numero //= 10

print(inverso)

# Retornando números primos
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = 50

for i in range(1, n + 1):
    if eh_primo(i) == True:
        print(i, end = " ")

# MDC e MMC
def calcular_mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calcular_mmc(a, b):
    mdc = calcular_mdc(a, b)
    return abs(a * b) // mdc 

# Triângulo de Asteriscos

altura = int(input("Digite aqui a altura da pirâmide"))

espacos = altura - 1
asteriscos = 1

while espacos >= 0:
    print(" " * espacos + "*" * asteriscos)
    espacos -= 1
    asteriscos += 2

# Imprimir um X 

tamanho = int(input("Digite aqui o tamanho do X(ímpar): "))

for i in range(n):
    linha = ""
    for j in range(n):
        if j == i or j == n - i - 1:
            linha += '*'
        else:
            linha += ' '
    print(linha)

# Palavra anagrama

def sao_anagramas(palavra_1, palavra_2):
    """Função para verificar se duas palavras são anagramas."""
    # Remover espaços e transformar em minúsculas para evitar problemas com letras maiúsculas/minúsculas
    palavra_1 = palavra_1.replace(" ", "").lower()
    palavra_2 = palavra_2.replace(" ", "").lower()

    # Comparar as contagens de cada letra
    return sorted(palavra_1) == sorted(palavra_2)

# Entrada das duas palavras
palavra_1 = input("Digite a primeira palavra: ")
palavra_2 = input("Digite a segunda palavra: ")

# Verificar se são anagramas e exibir o resultado
if sao_anagramas(palavra_1, palavra_2):
    print("As palavras são anagramas.")
else:
    print("As palavras NÃO são anagramas.")