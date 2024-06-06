arquivo = open("11-Leitura-de-Arquivo-Readline-While/11-desafio.txt", "r", encoding='utf-8')

while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()