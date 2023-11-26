def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def verificar_aprovacao(media, freq):
    if media >= 60 and freq >= 70:
        return "Aprovado"
    elif media < 60 and freq < 70:
        return "Reprovado por média e frequência"
    elif media < 60:
        return "Reprovado por média"
    elif freq < 70:
        return "Reprovado por frequência"

# {"Aluno": {"nota1": ..., "nota2": ..., "nota3": ..., "freq": ...}}
alunos = {}

while True:
    op = int(input("\n1. Adicionar aluno;\n2. Computar notas;\n3. Fechar\n"))
    
    if op == 1:
        nome = input("Nome do aluno: ")
        nota1 = float(input("Nota 1 do aluno: "))
        nota2 = float(input("Nota 2 do aluno: "))
        nota3 = float(input("Nota 3 do aluno: "))
        freq = float(input("Frequência do aluno: "))
        alunos[nome] = {"nota1": nota1, "nota2": nota2, "nota3": nota3, "freq": freq}

    elif op == 2:
        for nome, dados in alunos.items():
            print("\nAluno:", nome)
            media = calcular_media(dados["nota1"], dados["nota2"], dados["nota3"])
            print("Média de", media)
            resultado = verificar_aprovacao(media, dados["freq"])
            print(resultado)
            print("A frequência do aluno é", dados["freq"], "%.\n")
        break

    elif op == 3:
        break
