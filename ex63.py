termo1 = 0
termo2 = 1
termo3 = 0
i = 0
x = int(input('Quantos elementos voce quer imprimir?'))
print('{} --> {}'.format(termo1, termo2), end=' ')
while i < x:
    termo3 = termo1 + termo2
    print(" --> {} ".format(termo3), end=' ')
    termo1 = termo2
    termo2 = termo3
    i +=1
print('Fim')
