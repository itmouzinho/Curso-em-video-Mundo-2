i = 1
while True:
    num = int(input("Digite um numero para mostrar sua tabuada: "))
    if num < 0:
        break
    for i in range(1, 11):
        resultado = num*i
        print('{} X {} = {}'.format(num, i, resultado))
print("Fim")