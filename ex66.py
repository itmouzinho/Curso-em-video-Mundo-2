cont = soma = 0
num = int(input('Digite um numero: '))
while num != 999:
    if num == 999:
        break
    soma += num
    cont += 1
    num = int(input('Digite um numero: '))
print("Fim do programa, soma dos numeros foi {} e voce digitou {} vezes".format(soma , cont ))