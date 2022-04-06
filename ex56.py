idade = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
contmulher = 0
for i in range(1, 5):
    print('---------{}ª Pessoa---------'.format(i))
    nome = str(input('Digite seu nome: '))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo: ")).upper().strip()
    somaidade += idade
    ## aqui ele inicia o primeiro homem digitada como o mais velho
    if i == 1 and sexo == "M":
        maioridadehomem = idade
        nomevelho = nome
    if sexo == "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        contmulher += 1

mediaidade = somaidade/4
print('A media de idade eh {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print("mulher com menos de 20: {}.".format(contmulher))