letra_A = float(input())
letra_B = float(input())
letra_C = float(input())
area_trapezio = (letra_A + letra_B) * letra_C / 2
perimetro_triangulo = letra_A + letra_B + letra_C

if (letra_A < letra_B + letra_C) and (letra_B < letra_A + letra_C) and (letra_C < letra_A + letra_B):
    print(f"Perimetro = {perimetro_triangulo:.1f}")
else:
    print(f"Area = {area_trapezio:.1f}")