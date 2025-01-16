tamanho = int(input("Digite aqui o tamanho do losango: "))

ast_cima = 1
esp_cima = tamanho - 1

while esp_cima > -1:
    print((' ' * esp_cima) + ('*' * ast_cima))
    ast_cima += 2
    esp_cima -= 1

esp_baixo = 1
ast_baixo = ast_cima - 4

while esp_baixo <= tamanho - 1:
    print((' ' * esp_baixo) + ('*' * ast_baixo))
    ast_baixo -= 2
    esp_baixo += 1
