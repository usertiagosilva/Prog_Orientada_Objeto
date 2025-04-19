# Exercicio Final - Agenda de Contatos
from contato_agenda import Contact, ContactBook

# Instancia a agenda de contatos
contato_agenda = ContactBook()

# Loop principal do menu
while True:
    print("\nBem-vindo à Agenda de Contatos!")
    print("Escolha uma opção:")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Listar contatos")
    print("4. Buscar contato")
    print("5. Sair")
    print("______________________________")

    choice = input("Digite sua opção: ")

    if choice == "1":
        # Coleta os dados do contato
        name = input("Digite o nome do contato: ")
        phone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")

        # Cria e adiciona o contato
        contact = Contact(name, phone, email)
        contato_agenda.add_contact(contact)
        print(f"Contato {contact.name} adicionado com sucesso!")

    elif choice == "2":
        # Solicita o nome para buscar e remover
        name = input("Digite o nome do contato a ser removido: ")
        contact = contato_agenda.search_contact(name)

        # Só remove se o contato for encontrado
        if contact:
            contato_agenda.remove_contact(contact)
            print(f"Contato {contact.name} removido com sucesso!")

    elif choice == "3":
        # Exibe todos os contatos cadastrados
        contato_agenda.display_contact()

    elif choice == "4":
        # Busca contato pelo nome
        name = input("Digite o nome do contato a ser buscado: ")
        contato_agenda.search_contact(name)

    elif choice == "5":
        # Encerra o programa
        print("Saindo da agenda de contatos.")
        break

    else:
        # Opção inválida
        print("Opção inválida. Escolha uma opção de 1 a 5.")
