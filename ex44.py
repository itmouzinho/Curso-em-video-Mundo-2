valor = float(input('digite o valor do produto: '))
pagamento = int(input('''digite a forma de pagamento:
 1 - dinheiro, 
 2 - cartao a vista, 
 3 - cartao 2x, 
 4 - cartao 3x ou mais: '''))

if pagamento == 1:
    valor = valor*0.9
    print('O valor a ser pago com 10% de desconto fica: {}'.format(valor))

elif pagamento == 2:
    valor = valor*0.95
    print('o valor a ser pago com 5% de desconto, fica: {}'.format(valor))

elif pagamento == 3:
    print('o valor a ser pago é: {}'.format(valor))

elif pagamento == 4:
    valor = valor*1.2
    print('o valor a ser pago é: {}'.format(valor))