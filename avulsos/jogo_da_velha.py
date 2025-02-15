tabuleiro = [["zero", "zero", "x"],
             ["zero", "zero", "zero"],
             ["x", "zero", "x"]]

venceu = False

print("Este é o tabuleiro: ")

for i in tabuleiro:
    print(i)

pergunta_1 = input("Você quer tentar ganhar fechando uma linha? (S/N): ")
# Se tiver como vencer pela linha...
if pergunta_1 == "S":
    for linha in tabuleiro:
        if linha.count("x") == 2 and linha.count("zero") == 1:
            linha[linha.index("zero")] = "x"  
            print("Jogada vencedora encontrada!")
            venceu = True

    if venceu == True:
        print("Você venceu o jogo fechando uma linha")
        print("O tabuleiro terminou assim: ")
        for i in tabuleiro:
            print(i)
    else:
        print("Não foi possível vencer fechando uma linha")
        pergunta_2 = input("Você quer tentar vencer fechando uma coluna?(S/N): ")
else:
    pergunta_2 = input("Você quer tentar vencer fechando uma coluna?(S/N): ")
# Se tiver como vencer pela coluna...

if venceu == False: 
    if pergunta_2 == 'S':
        contador_coluna = 0

        colunas = []

        while contador_coluna < len(tabuleiro[0]):
            coluna = []
            for i in range(len(tabuleiro)):
                coluna.append(tabuleiro[i][contador_coluna])
            colunas.append(coluna)    
            contador_coluna += 1

        for linha in colunas:
            if linha.count("x") == 2 and linha.count("zero") == 1:
                tabuleiro[linha.index("zero")][colunas.index(linha)] = "x"  
                print("Jogada vencedora encontrada!")
                venceu = True

        if venceu == True:
            print("Você venceu o jogo fechando uma coluna")
            print("O tabuleiro terminou assim: ")
            for i in tabuleiro:
                print(i)
        else:
            print("Não foi possível vencer fechando uma coluna")
            pergunta_3 = input("Você quer tentar vencer fechando uma diagonal?(S/N): ")
    else:
        pergunta_3 = input("Você quer tentar vencer fechando uma diagonal?(S/N): ")        

if venceu == False: 
    if pergunta_3 == 'S':                                
        if (tabuleiro[0][0] == "x" and tabuleiro[2][2] == "x" and tabuleiro[1][1]=="zero"):
            tabuleiro[1][1] = "x"
            print("Você venceu o jogo fechando uma diagonal")
            print("O tabuleiro terminou assim: ")
            for i in tabuleiro:
                print(i)
            venceu = True
        elif (tabuleiro[0][2]=="x" and tabuleiro[2][0]=="x" and tabuleiro[1][1]=="zero"):
            tabuleiro[1][1] = "x"
            print("Você venceu o jogo fechando uma diagonal")
            print("O tabuleiro terminou assim: ")
            for i in tabuleiro:
                print(i)
            venceu = True
        else:
            print("Que pena! Parece que não é possível resolver o problema")
