#faça um programa que receba um valor como salário;
#faça um programa que receba a porcentagem de aumento;
#exiba o valor total após o aumento no interpretador.

salario = float(input("Digite o seu salário: "))
aumento = int(input("Digite a sua porcentagem de aumento: "))


novo_salario = salario + (salario * (aumento/100))

print("O seu novo salário é de R$%.2f" % novo_salario)


