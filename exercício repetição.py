#Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido 
# e continue pedindo até que o usuário informe um valor válido.

x = 0


while x < 1:
    nota = float(input("Digite a sua nota: "))
    
    print(nota)

    if nota > 10:
        print("Nota incorreta")

    nota = nota + 1