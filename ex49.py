num = int(input("Digite um numero: "))
i = 1
for i in range(0, 11):
    resultado = num * i
    print("{} X {} = {}".format(num, i, resultado))
    i += 1