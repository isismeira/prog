venceu = False

def vertical(i, j, palavra, jogo):
    palavra_vertical = []
    for x in range(i, i + len(palavra)):
            palavra_vertical.append(jogo[x][j])
    if palavra_vertical == palavra:
        print(f"O jogo pode ser fechado com uma linha vertical, começando pela linha {i+1} e coluna {j+1}")
        venceu = True
    else:
        horizontal(i, j, palavra, jogo)     

def horizontal(i, j, palavra, jogo):
     palavra_horizontal = []
     for x in range(j, j + len(palavra)):
            palavra_horizontal.append(jogo[i][x])
     if palavra_horizontal == palavra:
        print(f"O jogo pode ser fechado com uma linha horizontal, começando pela linha {i+1} e coluna {j+1}")
        venceu = True
     else:
          diagonal_d(i, j, palavra, jogo)

# obs. lógica para a diagonal
def diagonal_d(i, j, palavra, jogo):
    palavra_diagonal_d = []
    for k in range(len(palavra)):
        palavra_diagonal_d.append(jogo[i + k][j + k])
    if palavra_diagonal_d == palavra:
        print(f"O jogo pode ser fechado pela diagonal, começando pela linha {i+1} e coluna {j+1}")         

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
                           try:
                                diagonal_d(i, j, palavra, jogo)
                                if venceu == True:
                                     break
                           except IndexError:
                                print("Não foi possível solucionar o jogo")


jogo = [["c","s","x","d"],
        ["v","a","x","m"],
        ["x","s","s","s"],
        ["b","a","b","a"]]

palavra = ["c","a","s","a"]

verificar_jogo(jogo, palavra)

