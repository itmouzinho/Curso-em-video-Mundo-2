sexo = str(input("Digite seu sexo [M / F]: ")).strip().upper()
while sexo not in "MF":
    sexo = str(input("Digite seu sexo [M / F]: ")).strip().upper()
print('Programa concluido com sucesso')