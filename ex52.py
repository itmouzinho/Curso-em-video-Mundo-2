num = int(input("Digite um numero: "))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=" ")
    print(i, end=" -> ")
print("o numero {} foi dividido {} vezes".format(num, cont))
if cont == 2:
    print("O numero eh primo")
else:
    print("Nao eh primo")