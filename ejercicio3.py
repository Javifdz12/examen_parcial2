from ejercicio1 import pokemon
coach1=[]
sep=","
archivo1="coach_1_pokemons.csv"
with open(archivo1) as archivo:
    for linea in archivo:
        linea=linea.rstrip("/n")
        columnas=linea.split(sep)
        id=columnas[0]
        nombre=columnas[1]
        arma=columnas[2]
        salud=columnas[3]
        ataque=columnas[4]
        defensa=columnas[5]
        coach1.append(pokemon(id,nombre,arma,int(salud),int(ataque),int(defensa)))

coach2=[]
sep=","
archivo2="coach_2_pokemons.csv"
with open(archivo2) as archivo:
    for linea in archivo:
        linea=linea.rstrip("/n")
        columnas=linea.split(sep)
        id=columnas[0]
        nombre=columnas[1]
        arma=columnas[2]
        salud=columnas[3]
        ataque=columnas[4]
        defensa=columnas[5]
        coach2.append(pokemon(id,nombre,arma,int(salud),int(ataque),int(defensa)))

print(coach1)
print(coach2)

class entrenador:
    def __init__(self, list_pokemons):
        self.list_pokemons = list_pokemons
        self.pokemon1=list_pokemons[0]
        self
class combate_pokemon:
    def __init__(self,entrenador1,entrenador2):
        self.entrenador1=entrenador1
        self.entrenador2=entrenador2
    def comenzar(self):
        for pokemon1,pokemon2 in self.entrenador1,self.entrenador2:

            while pokemon1.salud>0 and pokemon2.salud>0:
                pokemon1.atacar(pokemon2)
                pokemon2.atacar(pokemon1)
            else:
                if pokemon1.salud<=0:
                    print(f"el pokemon {pokemon2.nombre} de {self.entrenador2} gano la batalla")
                    self.entrenador1.remove(pokemon1)
                elif pokemon2.salud<=0:
                    print(f"el pokemon {pokemon1.nombre} de {self.entrenador1} gano la batalla")
                    self.entrenador2.remove(pokemon2)





combate=combate_pokemon(coach1,coach2)
combate.comenzar()

