#  Exercício 2 - Crie uma classe chamada Product com os atributos name e price.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"Produto {self.name} - custa R$ {self.price} reais."
    
    def discount(self, perc_discount):
        valorDiscount = self.price * (perc_discount / 100)
        finalPrice = self.price - valorDiscount
        return f"O produto {self.name} com desconto de {perc_discount}% custa R$ {finalPrice} reais."
        

# Instanciando um objeto da classe Produto:   
xbox = Product("Xbox Series X", 4500)
iphone = Product("Iphone 12", 8000)
print(xbox)
print(iphone)
print(xbox.discount(10))
print(iphone.discount(20))
    