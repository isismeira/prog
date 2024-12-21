venceu = False

def vertical(i, j, palavra, jogo):
    palavra_vertical = []
    for x in range(i, i + len(palavra)):
            palavra_vertical.append(jogo[x][j])
    if palavra_vertical == palavra:
        print(f"O jogo pode ser fechado com uma linha vertical, começando pela linha {i+1} e coluna {j+1}")
        venceu = True
        print(venceu)
    else:
        horizontal(i, j, palavra, jogo)     

def horizontal(i, j, palavra, jogo):
     palavra_horizontal = []
     for x in range(j, j + len(palavra)):
            palavra_horizontal.append(jogo[i][x])
     if palavra_horizontal == palavra:
        print(f"O jogo pode ser fechado com uma linha horizontal, começando pela linha {i+1} e coluna {j+1}")
        venceu = True
        print(venceu)
     else:
          print("O jogo não pode ser fechado nem pela horizontal nem pela vertical")

def verificar_jogo(jogo, palavra):
    for i in range(len(jogo)):
        for j in range(len(jogo[0])):
            if jogo[i][j] == palavra[0]:
                 try:
                    vertical(i, j, palavra, jogo)
                    if venceu == True:
                         break
                 except IndexError:
                    try:
                        horizontal(i, j, palavra, jogo)
                        if venceu == True:
                             break 
                    except IndexError:
                           print("Não é possível fechar o jogo nem com uma linha horizantal ou vertical")          

jogo = [["a","b","x","d"],
        ["v","f","x","m"],
        ["c","a","s","a"],
        ["b","v","c","l"]]

palavra = ["c","a","s","a"]

verificar_jogo(jogo, palavra)

