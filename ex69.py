homem = mulher = anos18 =0
while True:
    idade = int(input("Digite uma idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Digite o sexo [F] / [M]: ")).upper().strip()
    if idade >= 18:
        anos18 += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade < 20:
        mulher += 1
    opcao = ' '
    while opcao not in "SN":
        opcao = str(input("Deseja cadastrar mais alguem? [S]/[N]")).upper().strip()[0]
    if opcao == "N":
        break
print(f'o total de maiores de 18 é de: {anos18}')
print(f'o total de homem é de {homem}')
print(f'o total de mulheres menor de 20 eh de: {mulher}')