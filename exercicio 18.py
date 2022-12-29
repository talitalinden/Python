#crie um programa que receba o saldo de uma conta bancária com R$359,56;
#depois insira uma nova quantia por meio de input;
#remova um valor de 125,98 referente a fatura de cartão de crédito;
#imprima o valor final da conta após as operações com string dinâmica.

saldo = 359.56
saldo2 = float(input("Digite o valor do seu saldo: "))
cartao = (saldo - saldo2)

print("Seu valor é %.2f e depois do pagamento do cartão ficou %.2f " % (saldo2, cartao))