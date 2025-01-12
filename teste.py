def selection_sort(array):
    for i in range(0, len(array) - 1):
        indice_minimo_atual = i
        for j in range(i+1, len(array)):
            if array[j] < array[indice_minimo_atual]:
                indice_minimo_atual = j

        array[i], array[indice_minimo_atual] = array[indice_minimo_atual], array[i]

array = [2, 6, 7, 4, 9, 3]
selection_sort(array)
print(array)   