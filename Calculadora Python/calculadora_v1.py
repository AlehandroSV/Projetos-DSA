print("\n******************* Python Calculator *******************")
print("Selecione o número da operação desejada: \n")
print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")

selec = int(input("Digite sua opção (1/2/3/4): "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if (selec == 1):
    res = n1 + n2
    print('{} + {} = {:.0f}'.format(n1, n2, res))
elif (selec == 2):
    res = n1 - n2
    print('{} - {} = {:.0f}'.format(n1, n2, res))
elif (selec == 3):
    res = n1 * n2
    print('{} x {} = {:.0f}'.format(n1, n2, res))
elif (selec == 4):
    res = n1 // n2
    print('{} / {} = {:.0f}'.format(n1, n2, res))
else:
    print("Seleção de operação incorreta!")