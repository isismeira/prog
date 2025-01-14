# Pesquisa Binária
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo+ alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None

minha_lista = [2, 5, 7, 16, 19]


print(pesquisa_binaria(minha_lista, 16))
 
# Bubble Sort
lista = [3, 5, 9, 2, 9]

for i in range(0, len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j] , lista[i]

print(lista)

# Reproduzir uma matriz nova, baseada no dobro da primeiro
matriz = [[1, 2, 3],
          [3, 4, 8]]

matriz_nova = []

for i in range(2*(len(matriz))):
    linha = [0] * (2 * len(matriz[0]))
    matriz_nova.append(linha)

for i in range(len(matriz_nova)):
    for j in range(len(matriz_nova[0])):
        matriz_nova[i][j] = matriz[i//2][j//2]

for linha in matriz_nova:
    print(linha)


# Escolas em um raio
import math

def calcular_distancia(x1, y1, x2, y2):
    """Calcula a distância entre dois pontos (x1, y1) e (x2, y2) em uma superfície plana."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def filtrar_escolas_por_raio(arquivo_entrada, arquivo_saida, ponto_x, ponto_y, raio):
    """Lê um arquivo com dados das escolas e filtra as escolas dentro do raio especificado."""
    escolas_no_raio = []
    
    with open(arquivo_entrada, 'r') as arquivo:
        for linha in arquivo:
            # Separar os dados por vírgula (supondo um formato: nome, bairro, rua, latitude, longitude)
            nome, bairro, rua, latitude, longitude = linha.strip().split(',')
            latitude = float(latitude)
            longitude = float(longitude)
            
            # Calcular a distância do ponto de referência
            distancia = calcular_distancia(ponto_x, ponto_y, latitude, longitude)
            
            # Verificar se a escola está dentro do raio
            if distancia <= raio:
                escolas_no_raio.append(f"{nome},{bairro},{rua},{latitude},{longitude}")
    
    # Escrever as escolas dentro do raio em um novo arquivo
    with open(arquivo_saida, 'w') as arquivo:
        for escola in escolas_no_raio:
            arquivo.write(escola + '\n')

# Exemplo de uso
arquivo_entrada = 'escolas.txt'  # Arquivo de entrada
arquivo_saida = 'escolas_filtradas.txt'  # Arquivo de saída
ponto_x = 10.0  # Coordenada x (latitude)
ponto_y = 20.0  # Coordenada y (longitude)
raio = 5.0  # Raio em quilômetros

filtrar_escolas_por_raio(arquivo_entrada, arquivo_saida, ponto_x, ponto_y, raio)
 