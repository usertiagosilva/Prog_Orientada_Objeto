# Avaliação e Média da Nota de Filmes
class Movie:
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0
        
    # Metodo Para retornar o objeto como string
    def __str__(self):
        return f"Filme: {self.name}"
    
    def techinical_sheet(self):
        print("## Dados do filme ##")
        print(f" Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Esta no plano? {self.includedPlan}")
        print(f" Avaliação do filme: {self.totalEvaluation}")
        print(f"Duração do filme: {self.durationMinutes} minutos")
        print(f"Total de avaliadores: {self.evaluators}\n")
        
    def evaluate(self,note):
        self.totalEvaluation += note
        self.evaluators += 1
        
    def average(self):
        print(f"Média do filme {self.name}: {self.totalEvaluation / self.evaluators}\n")

# Instanciando objetos da classe Movie        
mario = Movie("Super Mario", 1993, True, 104)
avatar = Movie("Avatar", 2009, False, 162)
mario.evaluate(5.5)
mario.evaluate(9.5)
mario.techinical_sheet()
mario.average()
avatar.evaluate(8.5)
avatar.evaluate(7.5)
avatar.techinical_sheet()
avatar.average()
        
        

