# Classe que representa um contato individual
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        # Retorna uma representação legível do contato
        return f"Nome: {self.name}, Telefone: {self.phone}, Email: {self.email}"


# Classe que representa a agenda de contatos
class ContactBook:
    def __init__(self):
        # Inicializa uma lista vazia para armazenar os contatos
        self.contacts = []

    def add_contact(self, contact):
        # Adiciona um novo contato à agenda
        self.contacts.append(contact)

    def remove_contact(self, contact):
        # Remove o contato informado da agenda
        self.contacts.remove(contact)

    def display_contact(self):
        # Exibe todos os contatos cadastrados
        if not self.contacts:
            print("Nenhum contato encontrado.")
        else:
            for contact in self.contacts:
                print(contact)
                print("______________________________")

    def search_contact(self, name):
        # Busca um contato pelo nome (ignora maiúsculas/minúsculas)
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return contact
        print(f"Contato {name} não encontrado.")
        return None
