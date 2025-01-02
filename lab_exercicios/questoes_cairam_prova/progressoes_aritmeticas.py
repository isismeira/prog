# DIFÍCIL
# Progressões aritméticas
def particoes():
    N = int(input())
    v = list(map(int, input().split()))

    # Inicializa as variáveis
    resp = 0
    b = 0

    # Loop principal para resolver o problema
    i = 1
    while i < N:
        # Se a razão não é igual à razão entre os dois primeiros termos
        # da PA atual, devemos começar uma nova PA e indicar isso
        if v[i] - v[i - 1] != v[b + 1] - v[b]:
            # `b` indica a posição em que começa a PA
            b = i

            resp += 1
            # `i` é incrementado porque quaisquer dois elementos formam
            # uma PA e não precisamos comparar `b+1` com `b`
            i += 1
        i += 1

    resp += 1

    print(resp)

particoes()