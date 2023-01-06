renda = int(input("Digite a sua renda mensal: "))
if renda <= 2000:
    print("Você tem R$ 1000.00 de limite")
elif renda > 2000 and renda <= 4000:
    print("Você tem R$ 2000.00 de limite")
elif renda > 4000 and renda <= 10000:
    print("Você tem R$ 3.000.00 de limite") 
else:
    print("Entre em contato com o seu gerente.")