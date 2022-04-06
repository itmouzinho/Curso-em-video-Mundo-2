'''a1 = int(input("Digite um numero: "))
r = int(input("Digite a razão: "))
decimo = a1 + (10-1)*r
for i in range(a1, decimo + r, r):
    print(i)'''

a1 = int(input("Digite um numero: "))
r = int(input("Digite a razão: "))
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(' {} '.format(a1), end=' - ')
        a1 += r
        cont += 1
    mais = int(input('quantos termos a mais voce deseja mostrar?'))