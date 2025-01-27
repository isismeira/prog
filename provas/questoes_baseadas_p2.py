# 1) "Censurando palavras"
lista = ["Python", "diversão"]
palavras = []

with open("provas/textinho.txt", "rt", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    texto = texto.split()

    for palavra in texto:
        nova_palavra = palavra.replace(",", "").replace(".", "")
        palavras.append(nova_palavra)

with open("provas/palavras_ocultas.txt", "wt", encoding="utf-8") as arquivo:
    for palavra in palavras:
        if palavra in lista:
            arquivo.write("***" + " ")
        else:
            arquivo.write(palavra + " ")
            
                