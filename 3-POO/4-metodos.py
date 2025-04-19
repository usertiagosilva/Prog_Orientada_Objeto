# Metodos são funções que pertencem a uma classe. Eles são chamados de funções de instância, porque são chamados em instâncias de uma classe. Eles podem ter argumentos, como qualquer outra função, e podem retornar valores, se necessário.

class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes 
        
    # Metodo Para retornar o objeto como string
    def __str__(self):
        return f"Filme: {self.name} - Ano de lançamento: {self.yearLaunch} - Incluso no plano: {self.includedPlan} - Nota: {self.note} - Duração: {self.durationMinutes} minutos"
    
    def techinical_sheet(self):
        print("## Dados do filme ##")
        print(f" Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Esta no plano? {self.includedPlan}")
        print(f" Avaliação do filme: {self.note}")
        print(f"Duração do filme: {self.durationMinutes} minutos\n")
        
mario = Movie("Super Mario", 2022, True, 9.5, 143)
top_gun = Movie("Top Gun", 2022, True, 7.5, 200)
matrix = Movie("Matrix", 2022, True, 8.5, 220)
mario.techinical_sheet()
top_gun.techinical_sheet()
matrix.techinical_sheet()
