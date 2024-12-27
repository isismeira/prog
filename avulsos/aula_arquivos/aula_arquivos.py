# Aula sobre Arquivos

# read -> lê arquivos com informações únicas
with open("avulsos/aula_arquivos/email.txt", "r") as arquivo:
    email = arquivo.read()
print(email)

# readlines -> para arquivos maiores
with open("avulsos/aula_arquivos/mensagem.txt", "r", encoding="utf-8") as arquivo:
    mensagem = arquivo.readlines()

print(mensagem)

for i in mensagem:
    print(i)

# write -> substitui por completo o texto que está escrito / se o arquivo não existir, cria um novo arquivo
with open("avulsos/aula_arquivos/senha.txt", "w") as arquivo:
    senha = arquivo.write("45678")

with open("avulsos/aula_arquivos/nova_senha.txt", "w") as arquivo:
    nova_senha = arquivo.write("101010")

# append -> adiciona uma nova informação no arquivo
with open("avulsos/aula_arquivos/email.txt", "a") as arquivo:
    novo_email = arquivo.write("\npythonimpressionador2@gmail.com")

