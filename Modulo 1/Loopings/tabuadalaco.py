
fator1 = int(input("Insira o número que deseja multiplicar: "))
fator2 = int(input("Insira o início do intervalo de sua tabuada: "))
limite = int(input('Insira o limite da sua tabuada: '))
for i in range (fator2, limite + 1):
    print(f'{fator1} x {i} = { fator1*i}')