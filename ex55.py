maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if i == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso lido foi de {} e o menor {}'.format(maior, menor))

