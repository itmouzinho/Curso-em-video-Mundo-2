peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Voce esta abaixo do peso')

elif imc >= 18.5 and imc < 25:
    print('Seu peso esta ideal')
elif imc >= 25 and imc < 30:
    print('sobrepeso')
elif imc >= 30 and imc < 40:
    print('obesidade')
elif imc >= 40:
    print('obesidade morbida')