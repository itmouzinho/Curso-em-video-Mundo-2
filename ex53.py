####Checando palindromo

frase = str(input("Digite uma frase: ")).upper().strip()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = ""
print('Voce digitou a frase {}'.format(palavras))

for letra in range(len(juntos) -1, -1, -1): ## pode tirar o for e colocar a seguinte expressao:
    inverso += juntos[letra]                   ### inverso = juntos[::-1]
if inverso == juntos:
    print('A frase é um palindro')
else:
    print('Nao eh')
