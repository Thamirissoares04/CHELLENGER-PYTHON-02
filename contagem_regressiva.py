import time
from datetime import datetime

# Definimos a data da próxima corrida
hora_corrida = datetime(2024, 6, 29, 18, 3, 0)

# Dicionário para armazenar corridas passadas
corridas_passadas = {
    "2023-01-15": "Corrida em Paris",
    "2023-03-22": "Corrida em Nova York",
    "2023-05-10": "Corrida em Roma"
}

# Matriz para armazenar informações sobre corridas
# Cada linha contém: [data, nome da corrida, duração estimada (em minutos)]
informacoes_corridas = [
    ["2023-01-15", "Corrida em Paris", 90],
    ["2023-03-22", "Corrida em Nova York", 120],
    ["2023-05-10", "Corrida em Roma", 100]
]

def contagem_regressiva(hora_corrida):
    while True:
        agora = datetime.now()
        tempo_restante = hora_corrida - agora
        
        if tempo_restante.total_seconds() <= 0:
            print("A corrida começou!")
            break
        
        dias = tempo_restante.days
        horas, segundos = divmod(tempo_restante.seconds, 3600)
        minutos, segundos = divmod(segundos, 60)

        mensagem = (f'Próxima corrida em: {hora_corrida.strftime("%d/%m/%Y %H:%M:%S")}' )
        mensagem += (f' | Tempo restante: {dias}d {horas}h {minutos}m {segundos}s')

        print(mensagem, end='\r', flush=True)
        
        time.sleep(1)

# Exibir corridas passadas
print("\nCorridas passadas:")
for data, nome, duracao in informacoes_corridas:
    print(f"Data: {data} | Nome: {nome} | Duração Estimada: {duracao} minutos")

# Exibir corridas em dicionário
print("\nCorridas Passadas (Dicionário):")
for data, nome in corridas_passadas.items():
    print(f"Data: {data} | Nome: {nome}")

contagem_regressiva(hora_corrida)
