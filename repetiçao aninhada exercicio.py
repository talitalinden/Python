#criar um programa que defina se um número é primo ou não.

numero = int(input("Digite um número: "))

divisao = 0
contador = numero

while contador > 0:
    if numero % contador == 0:
        divisao = divisao + 1
    
    contador = contador - 1

if divisao == 2:
    print("O número %d é primo." % numero)

else:
    print("O número %d não é primo." % numero)