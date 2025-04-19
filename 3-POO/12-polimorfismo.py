# Polimorfismo  - é um conceito de programação orientada a objetos que permite que diferentes classes sejam tratadas como instâncias da mesma classe através de uma interface comum. O polimorfismo permite que métodos com o mesmo nome possam ser usados em diferentes classes, desde que essas classes implementem esses métodos de maneira apropriada.

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
    
    def discount(self):
        return self._price * 0.1

class  Smartphone(Phone):
    # Método construtor
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price) # Chama o construtor da classe pai
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera
        
    def discount(self):
        return self._price * 0.15

moto = Phone('Motorola', 'Moto G', 1500)
print(moto)
moto.make_a_call(123456789)
print(f"Valor do {moto._brand} {moto._model_name}: R$ {moto._price}")
print(vars(moto))
print(moto.discount())
print('---------------------------------')

iphone = Smartphone('Apple', 'iPhone 14', 12000, '8GB', '256GB', '12MP')
print(iphone)
iphone.make_a_call('987654321')
print(f"Valor do {iphone._brand} {iphone._model_name}: R$ {iphone._price}")
print(vars(iphone))
print(iphone.discount())
print('---------------------------------')