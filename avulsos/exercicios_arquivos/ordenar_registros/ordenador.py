def classificar_registros(arquivo_entrada, arquivo_saida):
    # Ler o arquivo de entrada
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    # Separar os campos e transformar em uma lista de tuplas (nome, idade, nota)
    registros = [linha.strip().split(',') for linha in linhas]
    registros = [(nome, int(idade), float(nota)) for nome, idade, nota in registros]

    # Classificar os registros pela nota final em ordem decrescente
    registros_ordenados = sorted(registros, key=lambda x: x[2], reverse=True)

    # Escrever os registros ordenados no arquivo de saída
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
        for nome, idade, nota in registros_ordenados:
            arquivo.write(f"{nome},{idade},{nota:.1f}\n")


# Configurações
arquivo_entrada = 'alunos.txt'  # Nome do arquivo de entrada
arquivo_saida = 'estudantes_ordenados.txt'  # Nome do arquivo de saída

# Chamar a função
classificar_registros(arquivo_entrada, arquivo_saida)
