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
