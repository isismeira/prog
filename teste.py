with open('texto.txt', 'wt') as arquivo:
    matriz = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    
    for i in matriz:
        arquivo.write(','.join(map(str, i)) + '\n')