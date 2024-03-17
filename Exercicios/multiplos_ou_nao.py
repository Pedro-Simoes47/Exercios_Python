valor_A = int(input("Digite o valor de A:"))
valor_B = int(input("Digite o valor de B:"))

#estrutura  condicional tradicional
if valor_A % valor_B == 0 or valor_B % valor_A == 0:
    print("Sao multiplos")

else:
    print("Nao sao multiplos")
