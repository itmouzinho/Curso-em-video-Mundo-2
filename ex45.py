from random import randint

print("Inicio do jogo Jokenpô")

itens = ("Pedra", "Papel", "Tesoura")

computador = randint(0, 2)

print('''Escolha uma das opções: 
[1] Pedra, 
[2] Papel  
[3] Tesoura''')

usuario = int(input("Qual é sua jogada?"))

print("Computador jogou {}".format(itens[computador]))
print("Usuario jogou {}".format(itens[usuario]))

if computador == 0 and usuario == 0: ### outra maneira eh botar os ifs dentro dos ifs. tentar dps
    print('empate')
elif computador == 0 and usuario == 1:
    print('usuario vencey')
elif computador == 0 and usuario == 2:
    print('pc venceu')
elif computador == 2 and usuario == 2:
    print('empate')
elif computador == 2 and usuario == 1:
    print('pc ganhou')
elif computador == 2 and usuario == 0:
    print('usuario venceu')
elif computador == 1 and usuario == 1:
    print('empate')
elif computador == 1 and usuario == 0:
    print('pc ganhou')
elif computador == 1 and usuario == 2:
    print('usuario ganhou')