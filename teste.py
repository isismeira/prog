def sao_anagramas(palavra_1, palavra_2):
    """Função para verificar se duas palavras são anagramas."""
    # Remover espaços e transformar em minúsculas para evitar problemas com letras maiúsculas/minúsculas
    palavra_1 = palavra_1.replace(" ", "").lower()
    palavra_2 = palavra_2.replace(" ", "").lower()

    # Comparar as contagens de cada letra
    return sorted(palavra_1) == sorted(palavra_2)

# Entrada das duas palavras
palavra_1 = input("Digite a primeira palavra: ")
palavra_2 = input("Digite a segunda palavra: ")

# Verificar se são anagramas e exibir o resultado
if sao_anagramas(palavra_1, palavra_2):
    print("As palavras são anagramas.")
else:
    print("As palavras NÃO são anagramas.")
