import random
aleatorio = random.randint(1,100)
adivinhado = 0 
tentativas = 0
while adivinhado != aleatorio:
    adivinhado = int(input('Chute um número entre 1 e 100: '))
    if adivinhado > aleatorio:
        print('O número correto é menor.')
    elif adivinhado < aleatorio:
        print("O núnero correto é maior.")
    else:
        print(f'Parabéns! Você acertou em {tentativas}! tentativa(s)')
    tentativas += 1