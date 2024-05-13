'''
    Implemente duas funcoes:
        - Uma para converter a temperatura de celsius para fahrenheit;
        - Outra para a converter a temperatura de fahrenheit para celsius;
'''


temp_informada = float(input("Informe a temperatura para ser convertida: "))


def celsius_fahrenheit(temperatura):
    temp_em_fahrenheit = 9 / 5 * temperatura + 32 #formula de conversao C para F

    print(f"Temperatura em Celsius: {temperatura:.1f}°C, Temperatura em Fahrenheit: {temp_em_fahrenheit:.1f}°F ")

def fahrenheit_celsius(temperatura):
    temp_em_celsius = (temperatura - 32) * 5/9 # formula de conversao F para C

    print(f"Temperatura em Fahrenheit: {temperatura:.1f}°F, Temperatura em Celsius: {temp_em_celsius:.1f}°C")

celsius_fahrenheit(temperatura=temp_informada) 
fahrenheit_celsius(temperatura=temp_informada)

