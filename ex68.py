from random import randint
v = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Escolha um numero entre 0 e 10: '))
    total = jogador + computador
    opcao = " "
    while opcao not in "PI":
        opcao = str(input("Escolha [I] se impar ou [P] se par: ")).upper().strip()[0]
    print(f"Voce jogou {jogador} e o computador jogou {computador}. Total de {total}")
    if opcao == "I":
        if total % 2 == 0:
            print("Computador venceu")
            break
        else:
            print("Jogador venceu")
            v += 1
    elif opcao == "P":
        if total % 2 == 0:
            print("Jogador venceu!")
            v += 1
        else:
            print("Computador venceu!")
            break
print(f'Fim de jogo, voce venceu {v} vezes')
