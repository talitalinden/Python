# crie um programa que receba o valor inteiro, que será considerado dinheiro;
# imprima na tela o número de cédulas entregues ao usuário;
# as notas disponíveis são 100, 50, 20, 10;
# entregue notas de maior valor para menor valor.

saque = int(input("Digite o valor do saque: "))

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota1 = 0

while saque > 0:
    while saque >= 100:
        nota100 = nota100 + 1
        saque = saque - 100
    while saque >= 50:
        nota50 = nota50 + 1
        saque = saque - 50
    while saque >= 20:
        nota20 = nota20 + 1
        saque = saque - 20
    while saque >= 10:
        nota10 = nota10 + 1
        saque = saque - 10
    while saque >= 5:
        nota5 = nota5 + 1
        saque = saque - 20
print("Você receberá %d notas de R$100,00, %d notas de R$50,00, %d notas de R$20,00, %d notas de R$10,00, %d notas de 5,00" % (nota100, nota50, nota20, nota10, nota5))
