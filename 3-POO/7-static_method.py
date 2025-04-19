"""
Características do método Estático:

1- O método estático nao utiliza o parâmetro referente a classe.
2- O método de classe pode acessar mas não modificar o estado da classe.
3- Usamos o decorator @staticmethod para criar um método de classe.

"""
class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail
        
    @staticmethod
    def courses_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Dominando Python", "Módulos e Pip", "POO"]
        elif trail == "Automação com python":
           courses = ["Automação com Python", "Web Scraping", "Selenium"]
        else:
            courses = ["A definir"]
        return courses
    
print(Course.courses_trail("Python Fundamentos"))
print(Course.courses_trail("Automação com python"))
print(Course.courses_trail("Python para iniciantes"))