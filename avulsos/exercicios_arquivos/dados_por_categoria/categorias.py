def agrupar_dados_por_categoria(arquivo_entrada, arquivo_saida):
    # Dicionário para armazenar o valor total por categoria
    categorias = {}

    # Ler o arquivo de entrada
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            # Separar os campos da linha
            produto, categoria, quantidade, preco = linha.strip().split(',')
            quantidade = int(quantidade)
            preco = float(preco)

            # Calcular o valor total do produto no estoque
            valor_total_produto = quantidade * preco

            # Somar o valor total à categoria correspondente
            if categoria in categorias:
                categorias[categoria] += valor_total_produto
            else:
                categorias[categoria] = valor_total_produto

    # Escrever os resultados no arquivo de saída
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
        for categoria, valor_total in categorias.items():
            arquivo.write(f"Categoria: {categoria}\n")
            arquivo.write(f"Valor Total: {valor_total:.2f}\n") 
            arquivo.write("\n")  # Adicionar uma linha em branco entre categorias

# Configurações
arquivo_entrada = 'produtos.txt'  # Arquivo de entrada
arquivo_saida = 'estoque_agrupado.txt'  # Arquivo de saída

# Chamar a função
agrupar_dados_por_categoria(arquivo_entrada, arquivo_saida)
