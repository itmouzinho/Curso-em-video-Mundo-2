from datetime import date

hj = date.today().year
nascimento = int(input("Digite o ano q vc nasceu: "))
idade = hj - nascimento

if idade == 18:
    print("voce precisa se alistar esse ano")

elif idade > 18:
    print('Voce ja passou do prazo!!! em {} anos'.format(idade - 18))

elif idade < 18:
    print("voce ainda nao precisa de alistar, so daqui a {} anos".format(18 - idade))