"""
Características do método de classe:

1- O método de classe utiliza o parâmetro referente a classe.
2- O método de classe pode acessar ou modificar o estado da classe.
3- Usamos o decorator @classmethod para criar um método de classe.

"""
# Método construtor
class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # Método de classe    
    @classmethod
    def from_text(cls,string):
        import re
        item = re.findall(r"é \w*", string)
        name = item[0][2:]
        price = item[1][2:]
        return cls(name, int(price))

   
wiiU = Console.from_text("Meu video game é wiiU e o preço é 1000 reais")
xboxOne = Console.from_text("Meu video game é Xboxone e o preço é 1500 reais")
print(wiiU.__dict__)
print(xboxOne.__dict__)