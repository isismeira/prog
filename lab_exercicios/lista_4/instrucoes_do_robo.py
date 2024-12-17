#) FÁCIL
# se atentar de como funciona o tratamento do SAME AS

testes = int(input())
contador = 1

while contador <= testes:
    instrucoes = int(input())

    contador_instrucoes = 0

    eixo = 0

    lista = [0] * instrucoes

    while contador_instrucoes < instrucoes:
        comando = input()
        if comando == "LEFT":
            eixo -= 1
            lista[contador_instrucoes] = comando
            contador_instrucoes += 1
        elif comando == "RIGHT":
            eixo += 1
            lista[contador_instrucoes] = comando
            contador_instrucoes += 1
        elif comando[0:7] == "SAME AS":
            comando = comando.split(" ")
            valor = int(comando[-1])
            if lista[valor-1] == "LEFT":
                eixo -= 1
                lista[contador_instrucoes] = lista[valor-1]
                contador_instrucoes += 1
            elif lista[valor-1] == "RIGHT":
                eixo += 1
                lista[contador_instrucoes] = lista[valor-1]
                contador_instrucoes += 1

    print(eixo)
    contador += 1
