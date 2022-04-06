from datetime import date
nascimento = int(input("Digite sua data de nascimento: "))
hj = date.today().year
idade = hj - nascimento
if idade <= 9:
    print("Categoria mirim")
elif idade > 9 and idade <= 14:
    print("Categoria infantil")
elif idade > 14 and idade <= 19:
    print("Categoria junior")
elif idade > 19 and idade <= 20:
    print('categoria senior')
elif idade > 20:
    print('categoria master')