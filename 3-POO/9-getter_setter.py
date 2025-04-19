# Getter - Para obter o valor de um atributo privado, usamos o método getter. Ele é um método público que retorna o valor do atributo privado.
# Setter - Para modificar o valor de um atributo privado, usamos o método setter. Ele é um método público que recebe um novo valor e o atribui ao atributo privado.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f"Nome: {self.name}, Salário: {self.__salary}")
        
    # Método para buscar dados
    def get_salary(self):
        return self.__salary
    
    # Método para modificar atributo privado
    def set_salary(self, salary):
        self.__salary = salary 
        
maria = Employee("Maria", 5000)
joao = Employee("João", 6000)
maria.show()
joao.show()
print("__________________________________")

# Alterando somente o nome do funcionário
maria.name = "Maria Silva"
joao.name = "João Silva"
maria.show()
joao.show()
print("__________________________________")

# Alterando o salário do funcionário utilizando metodo setter
maria.set_salary(7000)
joao.set_salary(8000)
maria.show()
joao.show()



