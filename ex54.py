from datetime import date

hj = date.today().year
menores = 0
maiores = 0
for i in range(0, 7):
    nascimento = int(input("Digite seu ano de nascimento: "))
    if hj - nascimento < 18:
        menores += 1
    elif hj - nascimento >= 18:
        maiores += 1
print('A quantidade de menores é de {} e a quantidade de maiores é de {}'.format(menores, maiores))