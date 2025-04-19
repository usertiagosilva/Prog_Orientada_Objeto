# Construtor é um método especial que é chamado quando um objeto é instanciado.
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
    
# Instanciando a classe Movie        
movie = Movie("Os vingadores", 2022, True, 9.5, 143)
movie2 = Movie("Batman", 2022, True, 7.5, 200)
movie3 = Movie("Superman", 2022, True, 8.5, 220)
print(movie.name)
print(movie2.name)
print(movie3.name)
print(movie)



