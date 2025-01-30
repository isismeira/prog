def remover_pontuacao(palavra, lista):
    historico_de_alteracoes = [palavra]
    for simbolo in lista:
        nova_string = historico_de_alteracoes[-1]
        atual_remocao = nova_string.replace(simbolo, "")
        historico_de_alteracoes.append(atual_remocao)
    palavra_totalmente_removida = historico_de_alteracoes[-1]
    return palavra_totalmente_removida

print(remover_pontuacao(',[]"texto.txt".}?', [',', '[', ']', '.', '}', '?']))