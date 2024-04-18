quantity_ordered = int(input("Informe quantos Kaleidoscopes voce gostaria de comprar: "))

if quantity_ordered > 0:
    total_sale = quantity_ordered * 5.00
    discount = total_sale * 0.10 if quantity_ordered > 1 else 0
    total_sale -= discount
    sale_taxed = total_sale * 0.07
    new_total = sale_taxed + total_sale
    print(f"{new_total:,.2f}")
else:
    total_sale = quantity_ordered * 5.00
    sale_taxed = total_sale * 0.07
    new_total = sale_taxed + total_sale
    print(f"{new_total:,.2f}")

