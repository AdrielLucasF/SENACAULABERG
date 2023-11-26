import random

# Gerando uma lista aleatória de 6 números entre 1 e 50
lista_aleatoria = [random.randrange(1, 50) for _ in range(6)]
print(lista_aleatoria)

def somar_numeros(lista):
    # Lista vazia
    if len(lista) == 0:
        return 0
    # Lista com mais de um elemento
    else:
        return lista[0] + somar_numeros(lista[1:])

resultado = somar_numeros(lista_aleatoria)
print(f"A soma dos números na lista é: {resultado}")
