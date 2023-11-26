contatos = {
    'Bob': {'telefone': '987-654-3210', 'email': 'bob@email.com'},
    'Alice': {'telefone': '123-456-7890', 'email': 'alice@email.com'}
}

# 01. Acessar as informações de contato de uma pessoa específica a partir do dicionário "contatos".
nome_busca = input("Digite o nome para obter informações de contato: ")
if nome_busca in contatos:
    print(f"Telefone de {nome_busca}: {contatos[nome_busca]['telefone']}")
    print(f"Email de {nome_busca}: {contatos[nome_busca]['email']}")
else:
    print(f"O contato {nome_busca} não existe.")

# 02. Adicionar novas pessoas e suas informações de contato ao dicionário "contatos".
novo_nome = input("\nNome do novo contato: ")
novo_telefone = input("Número de telefone do novo contato: ")
novo_email = input("Email do novo contato: ")

contatos[novo_nome] = {'telefone': novo_telefone, 'email': novo_email}

print(f"Contato {novo_nome} adicionado com sucesso.")
print(contatos[novo_nome], "\n")

# 03. Modificar as informações de contato de uma pessoa existente no dicionário "contatos".
nome_atualizar = input("Nome do contato a ser atualizado: ")

if nome_atualizar in contatos:
    opcao_atualizar = int(input("1 para atualizar Telefone\n2 para atualizar Email\nEscolha a opção: "))
    if opcao_atualizar == 1:
        novo_telefone = input("Insira o novo número: ")
        contatos[nome_atualizar]["telefone"] = novo_telefone
    elif opcao_atualizar == 2:
        novo_email = input("Insira o novo e-mail: ")
        contatos[nome_atualizar]["email"] = novo_email
    else:
        print("Insira uma opção válida.")
else:
    print("O contato não existe.")

print(contatos[nome_atualizar], "\n")

# 04. Excluir um contato específico do dicionário "contatos".
nome_deletar = input("Insira o nome do contato para deletar: ")

if nome_deletar in contatos:
    del contatos[nome_deletar]
    print(f"Contato {nome_deletar} removido com sucesso.")
else:
    print("O contato não existe.")

# 05. Desafio (+1 pt): listar todos os nomes de pessoas no dicionário "contatos" em ordem alfabética.
nomes_ordenados = sorted(contatos)
print("Nomes em ordem alfabética:", nomes_ordenados)
