agenda = {}
validacao = True

while validacao:
    menu = int(input("\nBem-vinde à agenda!\n1. Adicionar contatos;\n2. Listar contatos\n3. Pesquisar contato\n4. Sair\n"))

    if menu == 1:
        nome = input("\nNome do novo contato: ")
        telefone = input("Número de telefone do novo contato: ")
        agenda[nome] = {'telefone': telefone}
        print("\nContato", nome, "adicionado com sucesso!\n")

    elif menu == 2:
        print("\nLista de Contatos:")
        for nome, contato in agenda.items():
            print(f"Nome: {nome} -- Telefone: {contato['telefone']}")

    elif menu == 3:
        busca_nome = input("\nNome a ser pesquisado: ")
        if busca_nome in agenda:
            print(f"Nome: {busca_nome} -- Telefone: {agenda[busca_nome]['telefone']}")
        else:
            print("Contato não existe na agenda.")

    elif menu == 4:
        validacao = False
