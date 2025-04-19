# As instâncias são objetos criados a partir de classes.
class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0
    
# Primeiro filme
movie = Movie()
movie.name = "The Godfather"
movie.yearLaunch = 1972
movie.includedPlan = True
movie.note = 9.2
movie.durationMinutes = 175

print("## Dados do filme ##")
print(f" Nome do filme: {movie.name} \n Ano de lançamento: {movie.yearLaunch}")