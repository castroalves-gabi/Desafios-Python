arquivo = open("10-Leitura-de-Arquivo-Readlines-For/10-desafio.txt", "r", encoding='utf-8')

for linha in arquivo.readlines():
    print(linha)

arquivo.close()