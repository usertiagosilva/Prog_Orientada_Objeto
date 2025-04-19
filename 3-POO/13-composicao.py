# Composição é uma relação entre dois objetos onde um objeto contém outro objeto.
# Por exemplo, um carro tem um motor. Se o carro for destruído, o motor também será.

class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
class Fish(Animal):
        race = ""
               
class Parrots(Animal):
        color = ""
        
class Zoo:
    def __init__(self):
        self.animals_dict = {}
        
    def add_animal(self, animal):
        self.animals_dict[animal.name] = animal.category
        
    def total_of_category(self, category):
        result = 0
        for animal in self.animals_dict.values():
            if animal == category:
                result += 1
        return f" No nosso zoológico temos {result} animais da categoria {category}."
    
zoo = Zoo()
peixe = Fish("Nemo", "mamífero")
peixe2 = Fish("Dora", "mamífero")
peixe3 = Fish("Yudi", "mamífero")
print(vars(peixe))
papagaio = Parrots("Loro", "ave")
print(vars(papagaio))
zoo.add_animal(peixe)
zoo.add_animal(peixe2)
zoo.add_animal(peixe3)
zoo.add_animal(papagaio)
print(zoo.total_of_category("mamífero"))
print(zoo.total_of_category("ave"))