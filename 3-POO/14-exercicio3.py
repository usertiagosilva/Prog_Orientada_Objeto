# Exercicio 3 - Cadastro de Viagem
from exercicio3 import Trip
from datetime import datetime

# Criando os destinos com preços
trip0 = Trip("Lençóis Maranhenses", 1500.00)
trip1 = Trip("Chapada dos Veadeiros", 1800.00)
trip2 = Trip("Pantanal", 2000.00)
trip3 = Trip("Serra da Canastra", 1700.00)
trip4 = Trip("Chapada Diamantina", 1600.00)

list_trip = [trip0, trip1, trip2, trip3, trip4]

print("E aí viajante. Temos algumas ofertas para você!")
traveler = input("Qual o seu nome? ")

print(f"\nOlá {traveler}, temos 5 destinos incríveis esperando por você!")
for i, trip in enumerate(list_trip):
    print(f"[{i}] - {trip.destination} (R$ {trip.price:.2f})")

try:
    choice = int(input("\nEscolha o número do destino desejado: "))
    if 0 <= choice < len(list_trip):
        selected_trip = list_trip[choice]

        # Data da viagem
        date_input = input("Digite a data da viagem (formato DD/MM/AAAA): ")
        travel_date = datetime.strptime(date_input, "%d/%m/%Y").date()

        # Mostrar resumo
        print("\n--- Confirmação da Viagem ---")
        print(f"Nome: {traveler}")
        print(f"Destino: {selected_trip.destination}")
        print(f"Data: {travel_date.strftime('%d/%m/%Y')}")
        print(f"Preço: R$ {selected_trip.price:.2f}")
        print("Sua viagem foi cadastrada com sucesso! 🧳🌍")

        # salvar em arquivo
        with open("cadastros_viagem.txt", "a") as file:
            file.write(f"{traveler} - {selected_trip.destination} - {travel_date} - R$ {selected_trip.price:.2f}\n")

    else:
        print("Opção inválida.")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número válido.")

