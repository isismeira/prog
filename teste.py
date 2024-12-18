valores = input().split()

numero_postos = int(valores[0])
numero_carrinhos = int(valores[1])
numero_leituras = int(valores[2])

# Inicializa Listas de Controle
proximo_posto = [1] * (numero_carrinhos + 1)  # Próximo posto que cada carrinho deve visitar
postos_certos = [0] * (numero_carrinhos + 1)  # Contagem de postos corretos por carrinho
ordem_cronologica = []  # Lista de carrinhos na ordem de leitura

# Processamento das leituras
for i in range(numero_leituras):
    corredor, posto = map(int, input().split())
    if posto == proximo_posto[corredor]:  # Verifica se o carrinho passou pelo posto correto
        postos_certos[corredor] += 1  # Incrementa a contagem de postos corretos
        proximo_posto[corredor] = (posto % numero_postos) + 1  # Atualiza o próximo posto esperado
    ordem_cronologica.append(corredor)

# Ordenação dos carrinhos
carrinhos = list(range(1, numero_carrinhos + 1))
carrinhos.sort(key=lambda c: (-postos_certos[c], ordem_cronologica.index(c)))

# Saída
print(*carrinhos)