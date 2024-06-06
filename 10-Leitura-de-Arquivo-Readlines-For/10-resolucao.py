arquivo = open("8-Leitura-de-Arquivo-Readline/8-desafio.txt", "r", encoding='utf-8')

for linha in arquivo.readlines():
    print(linha)

arquivo.close()