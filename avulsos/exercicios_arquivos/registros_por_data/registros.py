def retornar_registros(arquivo_entrada, arquivo_saida, data_inicial, data_final):
    ano_i, mes_i, dia_i = data_inicial.strip().split('-')
    ano_f, mes_f, dia_f = data_final.strip().split('-')

    ano_i = int(ano_i)
    mes_i = int(mes_i)
    dia_i = int(dia_i)

    ano_f = int(ano_f)
    mes_f = int(mes_f)
    dia_f = int(dia_f)

    registros_no_intervalo = []

    with open(arquivo_entrada, 'rt', encoding='utf-8') as arquivo:

        for linha in arquivo:
            numero, data, preco, nome = linha.strip().split(',')
            ano, mes, dia = data.strip().split('-')
            ano = int(ano)
            mes = int(mes)
            dia = int(dia)

            if (ano_i <= ano <= ano_f) and (mes_i <= mes <= mes_f) and (dia_i <= dia <= dia_f):
                registros_no_intervalo.append(f"{numero},{data},{preco},{nome}")

    with open(arquivo_saida, 'wt', encoding='utf-8') as arquivo:
        for linha in registros_no_intervalo:
            arquivo.write(linha + '\n')       

arquivo_entrada = 'avulsos/exercicios_arquivos/registros_por_data/registros.txt'
arquivo_saida = 'avulsos/exercicios_arquivos/registros_por_data/saida_registros.txt'
data_inicial = '2025-01-01'
data_final = '2025-01-15'

retornar_registros(arquivo_entrada, arquivo_saida, data_inicial, data_final)