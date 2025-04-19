# Herança em Python
# A herança é um recurso da POO que permite criar uma nova classe a partir de uma classe existente.

#Classe pai - super classe - classe base
class Animal:
    name = ""
    size = ""
    color = ""
    
    
    def eat(self):
        print("Animal está se alimentando")

#classe filha - herança simples        
class Horse(Animal):
    race = ""
        
    def escape(self):
        print("Cavalo fugindo!")

#classe filha - herança simples        
class Lion(Animal):
    mane = ""
    
    def hunt(self):
        print("Leão caçando!")

# Instanciando a classe Animal        
h = Horse()
h.name = "Tufão"
h.color = "Preto"
print(h.name)
print(h.color)
h.escape()
h.eat()
print("__________________________________")

l = Lion()
l.name = "Simba"
l.color = "Amarelo"
print(l.name)
print(l.color)
l.hunt()
l.eat()