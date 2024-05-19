from datetime import time, timedelta, datetime

def calcular_tempo_jogo(hora_inicial, min_inicial, hora_final, min_final):
    inicio_jogo = datetime(2024, 5, 16, hora_inicial, min_inicial)
    final_jogo = datetime(2024, 5, 16, hora_final, min_final)

    if final_jogo <= inicio_jogo:
        final_jogo += timedelta(days=1)

    duracao = final_jogo - inicio_jogo

    if duracao < timedelta(minutes=1):
        return "Erro: A duração do jogo é menor que 1 minuto."
    elif duracao > timedelta(hours=24):
        return "Erro: A duração do jogo é maior que 24 horas."
    else:
        horas, minutos = divmod(duracao.seconds, 3600)
        minutos //= 60
        return f"Duração do jogo: {horas} horas e {minutos} minutos"

hora_inicial = int(input("Digite a hora inicial: "))
minuto_inicial = int(input("Digite o minuto inicial: "))
hora_final = int(input("Digite a hora final: "))
minuto_final = int(input("Digite o minuto final: "))

resultado = calcular_tempo_jogo(hora_inicial, minuto_inicial, hora_final, minuto_final)
print(resultado)
