pergunta = "S"
soma = media = maior = menor = cont = 0
while pergunta == "S":
    numero = int(input('Digite um numero: '))
    soma = soma + numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    pergunta = str(input('Deseja continuar? [S]/[N]')).upper().strip()
media = soma/cont
print('a media dos valores foi {}, o menor é {} e o maior é {}'.format(media, menor, maior))
