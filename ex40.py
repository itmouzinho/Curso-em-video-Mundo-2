nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Parabens, voce foi aprovado com media {}".format(media))
else:
    print("Infelizmente sua media foi {}, e por isso voce nao foi aprovado".format(media))