from math import pow as p

lados = [] 

for lado in range(3):
    lado = float(input("Digite um lado: "))
    lados.append(lado)

lados.sort(reverse=True)

lado_a, lado_b, lado_c = lados

if lado_a >= lado_b + lado_c:
    print("Nao forma um triangulo!!")

else:
    if p(lado_a, 2) == p(lado_b, 2) + p(lado_c, 2):
        print("Triangulo Retangulo!!")

    elif p(lado_a, 2) > p(lado_b, 2) + p(lado_c, 2):
        print("Triangulo Obtusangulo!!")

    elif p(lado_a, 2) < p(lado_b, 2) + p(lado_c, 2):
        print("Triangulo Acutangulo!!")

    if lado_a == lado_b == lado_c:
        print("Triangulo Equilatero!!")
        
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("Triangulo Isosceles!!")

