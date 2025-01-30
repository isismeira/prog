p = [1,2,3,10,5,6]
k = 3

for i in range(len(p)):
    soma = 0
    primeiro_indice = i - k + 1
    for j in range(k):
        if primeiro_indice < 0:
            soma += 0
            primeiro_indice += 1
        else:
            soma += p[primeiro_indice]
            primeiro_indice += 1
    print(f"PM {i} = {(soma/k)}")            