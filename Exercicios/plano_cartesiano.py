print("Digite dois valores e descubra em qual dos quadrantes Q1 Q2 Q3 Q4 ele se encontra!")

valor_X = float(input("Digite o primeiro valor: "))
valor_Y = float(input("Digite o segundo valor: "))

if valor_X == 0 and valor_Y == 0:
    print("Valor se encontra na origem!")
elif valor_X > 0 and valor_Y > 0:
    print("Valor se encontra no Q1")
elif valor_X < 0 and valor_Y > 0:
    print("Valor se encontra no Q2")
elif valor_X < 0 and valor_Y < 0:
    print("Valor se encontra no Q3")
elif valor_X > 0 and valor_Y < 0:
    print("Valor se encontra no Q4")
