# FÁCIL

testes = int(input())

for i in range(testes):
    numero_alunos = int(input())

    alunos = list(map(int, input().split()))

    sorted_alunos = sorted(alunos, reverse=True)

    nao_trocou = 0

    for i in range(len(alunos)):
        if alunos[i] == sorted_alunos[i]:
            nao_trocou += 1

    print(nao_trocou)      