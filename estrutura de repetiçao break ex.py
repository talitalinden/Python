#Crie um loop que exibe os números digitados do usuário na tela;
#O loop deve ser cancelado quando o usuário digitar 0.


x = 0

while x < 1:
    numero = int(input("Digite um número: "))

    print(numero)

    if numero == 0:
        break

print("Pausa para o break")


    