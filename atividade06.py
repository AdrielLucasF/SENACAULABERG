# Usando o for
numero = int(input("Insira um número inteiro positivo: "))
soma_for = 0

for i in range(1, numero + 1):
    if i % 3 == 0:
        soma_for += i

print("Soma total (for):", soma_for)

# Usando o while
numero_atual = numero
soma_while = 0

while numero_atual > 0:
    if numero_atual % 5 == 0:
        soma_while += numero_atual
    numero_atual -= 1

print("Soma total (while):", soma_while)
