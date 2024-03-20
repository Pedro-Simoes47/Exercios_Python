
print("Descubra em qual dos intervalos ([0,25], (25,50], (50,75], (75,100]) o valor que voce deseja se encontra!")


valor = float(input("Digite o valor: "))

if valor < 0 or valor > 100:
    print(f"{valor} se encontra fora do intervalo!")
    exit()
elif valor <= 25.0:
    print(f"{valor} se encontra no intervalo de [0,25]!")
elif valor <= 50.0:
    print(f"{valor} se encontra no intervalo de [25,50]!")
elif valor <= 75.0:
    print(f"{valor} se encontra no intervalo de [50,75]!")
elif valor <= 100.0:
    print(f"{valor} se encontra no intervalo de [75,100]!")