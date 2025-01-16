# 1) Somatório
def somatorio(numero):
    soma_digitos = 0
    while numero > 0:
        ultimo_digito = numero%10
        soma_digitos += ultimo_digito
        numero = numero//10
    if soma_digitos > 9:
        print(f"Somatório: {soma_digitos}")
        somatorio(soma_digitos)
    else:
        print(f"Somatório: {soma_digitos}")
        print(f"Resultado final: {soma_digitos}")

numero = int(input("Digite aqui o número"))
somatorio(numero)

# 2) Tabuleiro de Xadrez
lin = int(input())
col = int(input())

for i in range(lin):
    for j in range(col):
        if i % 2 == 0 and j % 2 == 0:
            print('x', end='')
        if i % 2 == 0 and j % 2 != 0:
            print('o', end='')
        if i % 2 != 0 and j % 2 != 0:
            print('x', end='')
        if i % 2 != 0 and j % 2 == 0:
            print('o', end='')
    print('\n', end='')

# 3) Gerador de triângulos
n = int(input("Digite o tamanho do triângulo: "))

for i in range(1, n + 1):
    espacos = ' ' * (n - i) 
    asteriscos = '*' * (2 * i - 1)
    print(espacos + asteriscos)

# 4) Meio triângulo invertido
asteriscos = int(input("Digite o tamanho do triângulo"))

espacos = 0

while asteriscos > 0:
    ast = '*' * asteriscos
    esp = ' ' * espacos
    print(esp + ast)
    asteriscos -= 1
    espacos += 1

# 5) Losango 
tamanho = int(input("Digite aqui o tamanho do losango: "))

ast_cima = 1
esp_cima = tamanho - 1

while esp_cima > -1:
    print((' ' * esp_cima) + ('*' * ast_cima))
    ast_cima += 2
    esp_cima -= 1

esp_baixo = 1
ast_baixo = ast_cima - 4

while esp_baixo <= tamanho - 1:
    print((' ' * esp_baixo) + ('*' * ast_baixo))
    ast_baixo -= 2
    esp_baixo += 1

# 6) X
n = int(input("Digite o tamanho do X (ímpar): "))

if n % 2 == 0:
    print("Por favor, insira um número ímpar.")
else:
    for i in range(n):
        linha = ""
        for j in range(n):
            if j == i or j == n - i - 1: 
                linha += "*"
            else:
                linha += " " 
        print(linha)

# 7) Triângulo de números
tamanho = int(input("Digite aqui o tamanho da pirâmide: "))

espacos = tamanho - 1
numeros = 2

while espacos >= 0:
    for i in range(espacos):
        print(' ', end='')
    for j in range(1, numeros):
        print(j, end='')
        print(' ', end='') 
    print('\n', end='')
    espacos -= 1
    numeros += 1

# 8) Triângulo de Pascal
def triangulo_de_pascal(n):
    triangulo = []

    for i in range(n):
        linha = [1]  
        if i > 0:
            for j in range(1, i):
                valor = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
                linha.append(valor)
            linha.append(1) 
        triangulo.append(linha)

    for i in range(n):
        espacos = ' ' * (n - i - 1)
        print(espacos + ' '.join(map(str, triangulo[i])))

linhas = int(input("Digite o número de linhas do Triângulo de Pascal: "))
triangulo_de_pascal(linhas)                       