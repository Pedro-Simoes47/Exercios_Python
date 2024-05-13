hora_inicial = int(input("Digite a hora em que o jogo se iniciou: "))
hora_final = int(input("Digite a hora em que o jogo acabou: "))

if hora_inicial < hora_final:
    duracao_jogo = hora_final - hora_inicial
    print(f"O jogo durou {duracao_jogo:.0f} hora(s)")
else:
    duracao_jogo = 24 - hora_inicial + hora_final
    print(f"O jogo durou {duracao_jogo:.0f} hora(s)")
    