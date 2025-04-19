class Movie:
    """Representa um filme com informações de título, ano, plano, duração e avaliações."""

    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        """Inicializa o filme com seus atributos principais."""
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0

    def __str__(self):
        """Retorna o nome do filme."""
        return f"Filme: {self.name}"
    
    def technical_sheet(self):
        """Retorna a ficha técnica do filme."""
        return (f"## Dados do Filme ##\n"
                f" Nome: {self.name}\n"
                f" Ano: {self.yearLaunch}\n"
                f" Plano: {'Sim' if self.includedPlan else 'Não'}\n"
                f" Avaliação Total: {self.totalEvaluation}\n"
                f" Duração: {self.durationMinutes} min\n"
                f" Avaliadores: {self.evaluators}\n")

    def evaluate(self, note):
        """Adiciona uma nota ao filme, validando o intervalo permitido (0-10)."""
        if 0 <= note <= 10:
            self.totalEvaluation += note
            self.evaluators += 1
        else:
            print(f"Nota inválida para {self.name}. Insira um valor entre 0 e 10.")

    def average(self):
        """Calcula e exibe a média das avaliações, se houver pelo menos uma."""
        if self.evaluators == 0:
            print(f"{self.name} ainda não foi avaliado.\n")
        else:
            print(f"Média de {self.name}: {self.totalEvaluation / self.evaluators:.2f}\n")

# Instâncias dos filmes
mario = Movie("Super Mario", 1993, True, 104)
avatar = Movie("Avatar", 2009, False, 162)

# Avaliações
mario.evaluate(5.5)
mario.evaluate(9.5)
avatar.evaluate(8.5)
avatar.evaluate(7.5)

# Exibição dos resultados
print(mario.technical_sheet())
mario.average()

print(avatar.technical_sheet())
avatar.average()
