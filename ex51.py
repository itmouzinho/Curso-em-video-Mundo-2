a1 = int(input("Digite um numero: "))
r = int(input("Digite a razão: "))
decimo = a1 + (10-1)*r
for i in range(a1, decimo + r, r):
    print(i)