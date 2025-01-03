# 1) Criando uma função que lê uma lista de palavras de um arquivo e remova todas as duplicatas

def remover_duplicatas(arq):
    with open(arq, "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()

    palavras_unicas = []

    for i in palavras:
        if i not in palavras_unicas:
            palavras_unicas.append(i)
        else:
            print(f"Removendo {i}...")    

    with open(arq, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(palavras_unicas)


arq = "exercicios_aula/palavras.txt"

remover_duplicatas(arq)