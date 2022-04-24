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
        self.pokemon2=list_pokemons[1]
        self.pokemon3=list_pokemons[2]
class combate_pokemon:
    def __init__(self,entrenador1,entrenador2):
        self.entrenador1=entrenador1
        self.entrenador2=entrenador2
    def comenzar(self):

            while self.entrenador1.pokemon1.salud>0 and self.entrenador2.pokemon1.salud>0:
                self.entrenador1.pokemon1.atacar(self.entrenador2.pokemon1)
                self.entrenador2.pokemon1.atacar(self.entrenador1.pokemon1)
            else:
                if self.entrenador1.pokemon1.salud<=0:
                    self.entrenador1.list_pokemons.remove(self.entrenador1.pokemon1)
                    print(f"el pokemon {self.entrenador2.pokemon1.nombre} de {self.entrenador2} gano la batalla")
                    print(f"le quedan {self.entrenador2.pokemon1.salud} puntos de salud")
                elif self.entrenador2.pokemon1.salud<=0:
                    print(f"el pokemon {self.entrenador1.pokemon1.nombre} de {self.entrenador1} gano la batalla")
                    print(f"le quedan {self.entrenador1.pokemon1.salud} puntos de salud")

            while self.entrenador1.pokemon2.salud>0 and self.entrenador2.pokemon2.salud>0:
                self.entrenador1.pokemon2.atacar(self.entrenador2.pokemon2)
                self.entrenador2.pokemon2.atacar(self.entrenador1.pokemon2)
            else:
                if self.entrenador1.pokemon2.salud<=0:
                    self.entrenador1.list_pokemons.remove(self.entrenador1.pokemon2)
                    print(f"el pokemon {self.entrenador2.pokemon2.nombre} de {self.entrenador2} gano la batalla")
                    print(f"le quedan {self.entrenador2.pokemon2.salud} puntos de salud")
                elif self.entrenador2.pokemon2.salud<=0:
                    print(f"el pokemon {self.entrenador1.pokemon2.nombre} de {self.entrenador1} gano la batalla")
                    print(f"le quedan {self.entrenador1.pokemon2.salud} puntos de salud")

            while self.entrenador1.pokemon3.salud>0 and self.entrenador2.pokemon3.salud>0:
                self.entrenador1.pokemon3.atacar(self.entrenador2.pokemon3)
                self.entrenador2.pokemon3.atacar(self.entrenador1.pokemon3)
            else:
                if self.entrenador1.pokemon3.salud<=0:
                    self.entrenador1.list_pokemons.remove(self.entrenador1.pokemon3)
                    print(f"el pokemon {self.entrenador2.pokemon3.nombre} de {self.entrenador2} gano la batalla")
                    print(f"le quedan {self.entrenador2.pokemon3.salud} puntos de salud")
                elif self.entrenador2.pokemon3.salud<=0:
                    print(f"el pokemon {self.entrenador1.pokemon3.nombre} de {self.entrenador1} gano la batalla")
                    print(f"le quedan {self.entrenador1.pokemon3.salud} puntos de salud")






combate=combate_pokemon(entrenador(coach1),entrenador(coach2))
combate.comenzar()
print(coach1)
