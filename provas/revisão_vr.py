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