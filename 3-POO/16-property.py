# Decorator property - em Python - são usados para definir métodos de acesso (getters e setters) para atributos de uma classe. Eles permitem encapsular a lógica de acesso e modificação de atributos, tornando o código mais limpo e fácil de entender.
# Exemplo de uso do decorator property:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Nome deve ser uam string")
        self._name = value
        
pessoa = Person("Maria", 15)
print(vars(pessoa))
            