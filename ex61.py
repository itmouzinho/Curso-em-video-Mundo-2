'''a1 = int(input("Digite um numero: "))
r = int(input("Digite a razão: "))
decimo = a1 + (10-1)*r
for i in range(a1, decimo + r, r):
    print(i)'''

a1 = int(input("Digite um numero: "))
r = int(input("Digite a razão: "))
cont = 1
while cont <= 10:
    print(' {} '.format(a1), end=' - ')
    a1 += r
    cont += 1
print('Fim')


