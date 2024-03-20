"""
Renda                           Imposto de Renda
de R$0.00 ate R$2000.0      ==>     ISENTO
de R$2000.01 ate R$3000.0   ==>     8%    
de R$3000.01 ate R$4500.0   ==>     18%
acima de R$4500.0           ==>     28%

"""

print("Calcule quanto de imposto deve ser pago.")

valor_salario = float(input("Digite seu salario: "))

if valor_salario <= 2000.00 and valor_salario >= 0:
    print("Voce e isento de pagar o Imposto de Renda!!!")
    # Nao precisa realizar calculo algum.

elif valor_salario > 2000.01 and valor_salario <= 3000.0:
    valor_imposto = (valor_salario - 2000.00) *0.08
    # Calcula 8% de 1000 ja que ate 2000 e isento

elif valor_salario > 3000.01 and valor_salario <= 4500.00:
    valor_imposto = (valor_salario - 3000.0) * 0.18 + 1000.0 * 0.08
    # Calcula 18% do que exede de 3000 e adiciona 8% de 1000 ja que ate 2000 e isento
    

elif valor_salario > 4500.00:
    valor_imposto = (valor_salario - 4500.0) * 0.28 + 1500.0 * 0.18 + 1000.0 * 0.08  
    # Calcula 28% do que exede de 4500 e adciona 18% de 1500 mais 8% de 1000 ja que ate 2000 e isento

print(f"O valor do imposto a se pago e de R${valor_imposto:,.2f}")
