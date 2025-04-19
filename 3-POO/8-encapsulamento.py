# Encapsulamento em Python - É um conceito de POO que visa proteger os atributos e métodos de uma classe, tornando-os privados. Isso significa que eles não podem ser acessados diretamente fora da classe, garantindo a integridade dos dados e evitando modificações indesejadas.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f"Nome: {self.name}, Salário: {self.__salary}")
        
maria = Employee("Maria", 2000)
joao = Employee("João", 1500)
maria.show()
joao.show()
print("__________________________________")
# Testando o encapsulamento
maria.__salary = 3000
maria.show()