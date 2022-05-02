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
    def __init__(self, list_pokemons, nombre):
        self.nombre = nombre
        self.list_pokemons = list_pokemons
        self.pokemon1=list_pokemons[0]
        self.pokemon2=list_pokemons[1]
        self.pokemon3=list_pokemons[2]
    def get_pokemon(self):
        lista1=self.list_pokemons
        i=0
        print(f'{self.nombre} debe elegir uno de sus pokemons:')
        for i in range(0,len(lista1)):
            print(f"\n{i}- {lista1[i].nombre}")
        x=int(input())
        print(f'{self.nombre} eligio a {lista1[x].nombre}')
        return int(x)


class combate:
    def __init__(self,pokemon1,pokemon2):
        self.pokemon1=pokemon1
        self.pokemon2=pokemon2
    def empezar(self):
        while self.pokemon1.salud>0 and self.pokemon2>0:
            self.pokemon1.atacar(self.pokemon2)
            self.pokemon2.atacar(self.pokemon1)
        else:
            if self.pokemon1.salud<=0:
                print(f"el pokemon {self.pokemon2.nombre} gano la batalla")
                print(f"le quedan {self.pokemon2.salud} puntos de salud")

            else:
                print(f"el pokemon {self.pokemon1.nombre} gano la batalla")
                print(f"le quedan {self.pokemon1.salud} puntos de salud")

class combate_pokemon:
    def __init__(self,entrenador1,entrenador2):
        self.entrenador1=entrenador1
        self.entrenador2=entrenador2
    def combate(pokemon1,pokemon2):
        while pokemon1.salud>0 and pokemon2.salud>0:
            pokemon1.atacar(pokemon2)
            pokemon2.atacar(pokemon1)
        else:
            if pokemon1.salud<=0:
                print(f"el pokemon {pokemon2.nombre} gano la batalla")
                print(f"le quedan {pokemon2.salud} puntos de salud")

            else:
                print(f"el pokemon {pokemon1.nombre} gano la batalla")
                print(f"le quedan {pokemon1.salud} puntos de salud")

    def comenzar(self):
        a=self.entrenador1.get_pokemon()
        b=self.entrenador2.get_pokemon()
        print("la batalla comienza en 3....,2....,1....")
        while self.entrenador1.list_pokemons!=[] and self.entrenador2.list_pokemons!=[]:
            combate1=combate_pokemon.combate(self.entrenador1.list_pokemons[a],self.entrenador2.list_pokemons[b])
            if self.entrenador1.list_pokemons[a].salud<=0:
                self.entrenador1.list_pokemons.remove(self.entrenador1.list_pokemons[a])
                if self.entrenador1.list_pokemons!=[]:
                    a=self.entrenador1.get_pokemon()
            else:
                self.entrenador2.list_pokemons.remove(self.entrenador2.list_pokemons[b])
                if self.entrenador2.list_pokemons!=[]:
                    b=self.entrenador2.get_pokemon()
        else:
            if self.entrenador1.list_pokemons==[]:
                print(f"{self.entrenador2.nombre} gano el combate")
                print("!!ENHORABUENA¡¡")
            else:
                print(f"{self.entrenador1.nombre} gano el combate")
                print("!!ENHORABUENA¡¡")


combate=combate_pokemon(entrenador(coach1,"javi"),entrenador(coach2,"ruben"))
combate.comenzar()

