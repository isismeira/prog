def remover_duplicados(arquivo_entrada, arquivo_saida): 
    registros_unicos = {}

    # Ler o arquivo de entrada
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            # Separar os campos
            id_, nome, email, idade = linha.strip().split(',')
            
            # Usar o email como chave para garantir unicidade
            if email not in registros_unicos:
                registros_unicos[email] = (id_, nome, email, idade)

    # Escrever os registros únicos no arquivo de saída
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
        for id_, nome, email, idade in registros_unicos.values():
            arquivo.write(f"{id_},{nome},{email},{idade}\n")


# Configurações
arquivo_entrada = 'registros.txt'  # Nome do arquivo de entrada
arquivo_saida = 'registros_unicos.txt'  # Nome do arquivo de saída

# Chamar a função
remover_duplicados(arquivo_entrada, arquivo_saida)
