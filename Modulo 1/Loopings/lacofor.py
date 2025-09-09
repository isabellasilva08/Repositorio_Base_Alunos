import random

print("SUPER JOGO DE ADIVINHAÇÃO DO NÚMERO MÁGICO.")

numero_magico = random.randint(1, 100)
tentativas = 0

while True:
    try:
        numero_adivinhacao = int(input("Digite um número entre 1 e 100: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    tentativas += 1

    if numero_adivinhacao == numero_magico:
        print(f"Parabéns, você acertou em {tentativas} tentativas!")
        break
    elif numero_adivinhacao > numero_magico:
        print("O número mágico é menor.")
    else:
        print("O número mágico é maior.")