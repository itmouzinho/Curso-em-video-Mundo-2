total = menor = contmil = 0
cont = 1
barato = ' '
while True:
    nomeprod = str(input('Digite o nome do produto: ')).upper().strip()
    preco = int(input('Digite o preco do produto: '))
    if cont == 1: # or preco < menor:
        menor = preco
        barato = nomeprod
    else: # este bloco pode ser eliminado colocando o "OR" no codigo acima
        if preco < menor:
            menor = preco
            barato = nomeprod
    if preco > 1000:
        contmil += 1
    total = total + preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Voce quer continuar? ')).upper().strip()
    if resp == "N":
        break
print(f'o total da compra foi de {total}')
print(f'temos {contmil} produtos custando mais de mil')
print(f'o produto mais barato custa: {menor} cujo nome eh {barato}')