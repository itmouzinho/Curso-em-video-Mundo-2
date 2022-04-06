num = int(input('digite um numero inteiro: '))
opcao = int(input("""Escolha a base de conversão: 
[1] binario 
[2] octal 
[3] hexadecimal"""))

if opcao == 1:
    print("voce converteu o numero {} para binario {}".format(num, bin(num)))

elif opcao == 2:
    print("voce converteu o numero {} para octal {}".format(num, oct(num)))

elif opcao == 3:
    print("voce converteu o numero {} para hexadecimal {}".format(num, hex(num)))

else:
    print("Operação nao aceita.")