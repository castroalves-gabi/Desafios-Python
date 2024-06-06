from datetime import datetime, timedelta

def obter_data_valida():
    while True:
        data_entrada = input("Digite uma data no formato dd-mm-yyyy: ")
        try:
            data_formatada = datetime.strptime(data_entrada, "%d-%m-%Y")
            return data_formatada
        except ValueError:
            print("Data inválida. Tente novamente.")

def obter_dias_valido():
    while True:
        try:
            dias = int(input("Quantos dias você quer acrescentar à data? "))
            return dias
        except ValueError:
            print("Número de dias inválido. Tente novamente.")

def main():
    data = obter_data_valida()
    dias_para_acrescentar = obter_dias_valido()
    data_final = data + timedelta(days=dias_para_acrescentar)
    
    data_final_str = data_final.strftime("%d-%m-%Y")
    print("Data final:", data_final_str)

if __name__ == "__main__":
    main()
