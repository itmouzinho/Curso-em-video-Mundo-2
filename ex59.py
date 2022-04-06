num1 = int(input('Digite o primeiro numero: '))
num2 = int(input("Digite o segundo numero: "))

opcao = 0

while opcao != 5:
    opcao = int(input('''Qual operação voce deseja realizar?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair'''))

    if opcao == 1:
        soma = num1 + num2
        print("O resultado é: {} ".format(soma))
        print("------------------------------")

    elif opcao == 2:
        mult = num1 * num2
        print("O resultado é: {} ".format(mult))
        print("------------------------------")

    elif opcao == 3:
        if num1 > num2:
            print('o maior numero é: {}'.format(num1))
            print("------------------------------")
        elif num1 == num2:
            print('Os dois numeros sao iguais')
            print("------------------------------")
        else:
            print('o maior numero é: {}'.format(num2))
            print("------------------------------")

    elif opcao == 4:
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input("Digite o segundo numero: "))
    elif opcao == 5:
        print('fim do programa')
    else:
        print('Opcao invalida')
print('Fora do loop')