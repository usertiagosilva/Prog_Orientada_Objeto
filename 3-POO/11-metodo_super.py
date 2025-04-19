# Método super - Herança Múltipla
# O método super() é usado para chamar métodos de uma classe pai.

class Phone:
    # Método construtor
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price
        
    # Metodo Para retornar o objeto como string   
    def __str__(self):
        return f'{self._brand} {self._model_name}'
    
    # Método estatico
    @staticmethod
    def make_a_call(phone_num):
        print(f'Ligando para {phone_num}...')

class  Smartphone(Phone):
    # Método construtor
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price) # Chama o construtor da classe pai
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera

moto = Phone('Motorola', 'Moto G', 1500)
print(moto)
moto.make_a_call(123456789)
print(f"Valor do {moto._brand} {moto._model_name}: R$ {moto._price}")
print(vars(moto))
print('---------------------------------')

iphone = Smartphone('Apple', 'iPhone 14', 12000, '8GB', '256GB', '12MP')
print(iphone)
iphone.make_a_call('987654321')
print(f"Valor do {iphone._brand} {iphone._model_name}: R$ {iphone._price}")
print(vars(iphone))
print('---------------------------------')