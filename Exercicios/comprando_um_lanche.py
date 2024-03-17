item = int(input("Digite o codigo do item desejado: "))

if item <= 0 or item >=6:
    print("Codigo invalido!!")
    exit() #encerra a execucao do programa caso digitem um codigo de item invalido.
    
quantidade = int(input("Digite a quantidade desejada do item: "))
total_da_compra = 0



if item == 1:
    total_da_compra = 4.00 * quantidade

elif item == 2:
    total_da_compra = 4.50 * quantidade

elif item == 3:
    total_da_compra = 5.00 * quantidade
    
elif item == 4:
    total_da_compra = 2.00 * quantidade
    
elif item == 5:
    total_da_compra = 1.50 * quantidade

print(f"O total da compra e de: R${total_da_compra}")