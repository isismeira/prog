def ordenar_matriz(m):
    for i in range(0, len(m)):
        for j in range(i+1, len(m)):
            if max(m[i]) > max(m[j]):
                m[i], m[j] = m[j], m[i]

    return m

matriz = [[1, 5, 5],
          [9, 3, 1],
          [1,2,3],
          [10,3,4],
          [4, 5, 3]]

print(ordenar_matriz(matriz))            