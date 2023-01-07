#crie um programa que imprima todos os números pares de 1 a 50.

numero = 1

while numero <= 50:
    if numero % 2 == 0: #aqui gera os multiplos, que consequentemente serão pares. E para números ímpares?
        print(numero)
    numero = numero + 1