from datetime import datetime

data_atual = "22-02-2024"

data_formatada = datetime.strptime(data_atual, "%d-%m-%Y")

print("Data atual:", data_formatada)
