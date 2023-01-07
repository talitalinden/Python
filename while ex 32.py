#crie um programa que imprima todos os números ímpares de 1 a 50.

numero = 1

while numero <= 50:
    if numero % 2 != 0: # != é sinal de diferença em python 
        print(numero)
    numero = numero + 1