from random import randint

computador = randint(0, 11)
jogador = int(input('Digite um numero: '))
cont = 0
while computador != jogador:
    computador = randint(0, 11)
    jogador = int(input('Que pena, voce errou, tente novamente: Digite um numero: '))
    cont += 1

print('Parabens voce ganhou o jogo, numero sorteado foi {} e voce jogou {}. Voce precisou de {} tentativas'.format(computador, jogador, cont))