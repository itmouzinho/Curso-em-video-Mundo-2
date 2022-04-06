casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salario: "))
anos = int(input("Digite em quantos anos voce pretende pagar: "))

prestacao = casa/(anos*12)

if prestacao > salario*0.3:
    print("Emprestimo negado, pois seu salario não é compativel com a prestacao de {:.2f}".format(prestacao))

elif prestacao <= salario*0.3:
    print("Parabens, voce vai conseguir financiar sua casa, com a prestacao de {:.2f}".format(prestacao))