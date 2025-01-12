def escreveMatriz(mat, file):
    with open(file, 'w') as f:
        for linha in mat:
            # Converte os elementos da linha para strings e os une com vírgulas
            f.write(','.join(map(str, linha)) + '\n')

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]            

arquivo = 'avulsos/saida.txt'

escreveMatriz(matriz, arquivo)