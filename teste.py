def simetrica(A):
    if len(A) != len(A[0]):
        print("A matriz não é simétrica (ela não é quadrada)")
    else:
        transposta = []
        for i in range(len(A)):
            transposta.append([0] * len(A))
        for i in range(len(transposta)):
            for j in range(len(transposta[0])):
                transposta[i][j] = A[j][i]         
        if transposta == A:
            print("A matriz é simétrica")
        else:
            print("A matriz não é simétrica")

matriz = [[1, 4, 5],
          [4, 2, 6],
          [5, 6, 3]]

simetrica(matriz)
