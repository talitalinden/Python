num = int(input("Digite um número: "))

if num > 10:
    print("Pode proceguir.")

    mult = num * 2
    mult2 = num * 5

    if num < 20:
        print("O resultado fica %d " % mult)
    else:
        print("O resultado é %d" % mult2)

else:
    print("Para proceguir, o número precisa ser maior que 10.")
