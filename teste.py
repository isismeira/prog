def maxLocal(matriz, n):
    if n % 2 == 0:
        raise ValueError("O tamanho da vizinhança n deve ser um número ímpar.")
    
    lista = []
    rows, cols = len(matriz), len(matriz[0])
    metade_n = n // 2

    # Itera por cada elemento que está na borda
    for i in range(metade_n, rows - metade_n):
        for j in range(metade_n, cols - metade_n): 
            # Verifica se cada elemento na vizinhança de matriz[i][j] é menor do que o mesmo
            eh_max_local = True
            # Itera por cada elemento da vizinhança de matriz[i][j]
            for k in range(i - metade_n, i + metade_n + 1):
                for l in range(j - metade_n, j + metade_n + 1):
                    if matriz[i][j] <= matriz[k][l] and (k != i or l != j):
                        eh_max_local = False
                        break
                if not eh_max_local:
                    break
            if eh_max_local:
                lista.append(matriz[i][j])
    
    return lista

matriz = [
    [1, 2, 3, 4, 5],
    [5, 10, 7, 12, 9],
    [9, 8, 9, 6, 5],
    [4, 3, 2, 14, 0],
    [0, 1, 2, 3, 4]
]

n = 3

resultado = maxLocal(matriz, n)
print(resultado)