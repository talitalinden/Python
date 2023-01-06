
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um outro número: "))
result = num1 * num2

if result <= 100:
    print("O número é baixo.")
else:
    print("O número %d é alto." % result)