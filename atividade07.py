num = int(input("Insira um número inteiro positivo: "))

if num < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    fatorial = 1

    for i in range(num):
        fatorial *= (i + 1)

    print("O fatorial de", num, "é", fatorial)
