peso_info = float(input("Informe o peso para ser convertido: "))

def libra_para_kilo(peso):
    peso_convertido = peso / 2.205 
    return f"Peso em Kgs: {peso_convertido:.2f}"

def kilo_para_libra(peso):
    peso_convertido = peso * 2.205
    return f"Peso em Lbs: {peso_convertido:.2f}"

print(libra_para_kilo(peso_info))
print(kilo_para_libra(peso_info))


