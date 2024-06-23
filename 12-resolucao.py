class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."

# Entrada de dados do usuário
nome = input().strip()  
numero = input().strip()  
plano = input().strip()  

# Criação do objeto UsuarioTelefone com os dados fornecidos
usuario = UsuarioTelefone(nome, numero, plano)

# Impressão da mensagem de sucesso
print(usuario)
