# a) Insertion Sort

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j-1] > array[j] and j > 0:
            array[j -1], array[j] = array[j], array[j-1]
            j -= 1

array = [2, 6, 5, 1, 3, 4]
insertion_sort(array)
print(array)

# b) Selection Sort

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

# c) Bubble Sort

def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

array = [2, 6, 7, 4, 9, 3]
bubble_sort(array)
print(array)