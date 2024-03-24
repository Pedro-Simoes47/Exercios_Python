nota_1 = float(input("Informe a primeira nota: "))
nota_2 = float(input("Informe a segunda nota: "))
nota_3 = float(input("Informe a terceira nota: "))
nota_4 = float(input("Informe a quarta nota: "))

media_final = ((nota_1 * 2) + (nota_2 * 3) + (nota_3 * 4) + (nota_4 * 1)) / 10

if media_final >= 7.0:
    print(f"\nMedia: {media_final:,.1f}\nAluno Aprovado!\n")
elif media_final <= 6.9 and media_final >= 5.0:
    print(f"\nMedia: {media_final:,.1f}\nAluno em exame!\n")
    recuperacao = float(input("Informe a nota da recuperacao: "))
    media_final = (media_final + recuperacao) / 2
    print(f"\nNota do Exame: {recuperacao:,.1f}")
    if media_final >= 5.0:
        print(f"\nAluno Aprovado!\nMedia Final: {media_final:,.1f}")
    else:
        print(f"\nAluno Reprovado!\nMedia Final: {media_final:,.1f}")
else:
    print(f"\nMedia: {media_final:,.1f}\nAluno Reprovado!\n")
