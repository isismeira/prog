# Palavras Cruzadas

jogo = [["a","b","c","d"],
        ["v","f","a","m"],
        ["g","d","s","q"],
        ["b","v","a","l"]]

palavra = ["c","a","s","a"]

palavra_vertical = []

palavra_horizontal = []

palavra_diagonal = []

for i in range(len(jogo)):
    for j in range(len(jogo[0])):
        if jogo[i][j] == palavra[0]:
            try:    
                for x in range(i, i + len(palavra)):
                    palavra_vertical.append(jogo[x][j])
                if palavra_vertical == palavra:
                    print(f"O jogo pode ser fechado com uma linha vertical, começando pela linha {i+1} e coluna {j+1}")
                    break
            except IndexError:
                try:
                    for x in range(j, j + len(palavra)):
                        palavra_horizontal.append(jogo[i][x])
                    if palavra_horizontal == palavra:
                            print(f"O jogo pode ser fechado com uma linha horizontal, começando pela linha {i+1} e coluna {j+1}")
                            break    
                except IndexError:
                                
             