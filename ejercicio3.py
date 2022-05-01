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
        for i in lista1[i]:
            x=input(f"{self.nombre} debe elegir uno de sus pokemons:\n{i}- {lista1[i]}")
            if x not in range(len(lista1)-1):
                x=input(f"{self.nombre} debe elegir una de las opciones numericas a continuacion:\n{i}- {lista1[i]}")
            else:
                print(f"el entrenador eligio a {lista1[x].nombre}")
        return x


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
    def comenzar(self):
            if self.entrenador1.get_pokemon()==0:

                if self.entrenador2.get_pokemon()==0:

                    while self.entrenador1.pokemon1.salud>0 and self.entrenador2.pokemon1.salud>0:
                        self.entrenador1.pokemon1.atacar(self.entrenador2.pokemon1)
                        self.entrenador2.pokemon1.atacar(self.entrenador1.pokemon1)
                    else:
                        if self.entrenador1.pokemon1.salud<=0:
                            self.entrenador1.list_pokemons.remove(self.entrenador1.pokemon1)
                            print(f"el pokemon {self.entrenador2.pokemon1.nombre} de {self.entrenador2.nombre} gano la batalla")
                            print(f"le quedan {self.entrenador2.pokemon1.salud} puntos de salud")
                            if self.entrenador1.get_pokemon()==0:
                                while self.entrenador1.list_pokemons[0].salud>0 and self.entrenador2.pokemon1.salud>0:
                                    self.entrenador1.list_pokemons[0].atacar(self.entrenador2.pokemon1)
                                    self.entrenador2.pokemon1.atacar(self.entrenador1.list_pokemons[0])
                                else:
                                    if self.entrenador1.list_pokemons[0].salud<=0:
                                        self.entrenador1.list_pokemons.remove(self.entrenador1.list_pokemons[0])
                                        print(f"el pokemon {self.entrenador2.pokemon1.nombre} de {self.entrenador2.nombre} gano la batalla")
                                        print(f"le quedan {self.entrenador2.pokemon1.salud} puntos de salud")
                                        print(f"A {self.entrenador1.nombre} solo le queda un pokemon")
                                        x=self.entrenador1.get_pokemon()
                                        while self.entrenador1.list_pokemons[x].salud>0 and self.entrenador2.pokemon1.salud>0:
                                            self.entrenador1.pokemon1.atacar(self.entrenador2.pokemon1)
                                            self.entrenador2.pokemon1.atacar(self.entrenador1.pokemon1)
                                        else:
                                            if self.entrenador1.list_pokemons[x].salud<=0:
                                                self.entrenador1.list_pokemons.remove(self.entrenador1.list_pokemons[x])
                                                print(f"el pokemon {self.entrenador2.pokemon1.nombre} de {self.entrenador2.nombre} gano la batalla")
                                                print(f"le quedan {self.entrenador2.pokemon1.salud} puntos de salud")
                                                print(f'{self.entrenador2.nombre} gano la batalla')
                                            elif self.entrenador2.pokemon1.salud<=0:
                                                self.entrenador2.list_pokemons.remove(self.entrenador2.pokemon2)
                                                print(f"el pokemon {self.entrenador1.list_pokemons[0]} de {self.entrenador1.list_} gano la batalla")
                                                print(f"le quedan {self.entrenador1.list_pokemons[0].salud} puntos de salud")
                                                if self.entrenador2.get_pokemon()==0:
                                                    while self.entrenador1.list_pokemons[x].salud>0 and self.entrenador2.pokemon1.salud>0:
                                                        self.entrenador1.pokemon1.atacar(self.entrenador2.pokemon1)
                                                        self.entrenador2.pokemon1.atacar(self.entrenador1.pokemon1)
                                                    else:
                                                        if self.entrenador1.list_pokemons[x].salud<=0:
                                                            self.entrenador1.list_pokemons.remove(self.entrenador1.list_pokemons[x])
                                                            print(f"el pokemon {self.entrenador2.pokemon1.nombre} de {self.entrenador2.nombre} gano la batalla")
                                                            print(f"le quedan {self.entrenador2.pokemon1.salud} puntos de salud")
                                                            print(f'{self.entrenador2.nombre} gano la batalla')
                                                        elif self.entrenador2.pokemon1.salud<=0:
                                                            self.entrenador2.list_pokemons.remove(self.entrenador2.pokemon2)
                                                            print(f"el pokemon {self.entrenador1.list_pokemons[0]} de {self.entrenador1.list_} gano la batalla")
                                                            print(f"le quedan {self.entrenador1.list_pokemons[0].salud} puntos de salud")
                                                            print(f'A {self.entrenador2.nombre} le queda solo un pokemon')
                                                            x=self.entrenador2.get_pokemon()
                                                            while self.entrenador2.list_pokemons[x].salud>0 and self.entrenador1.pokemon1.salud>0:
                                                                self.entrenador1.pokemon1.atacar(self.entrenador2.pokemon1)
                                                                self.entrenador2.list_pokemons[x].atacar(self.entrenador1.list_pokemons[x])
                                                            else:
                                                                if self.entrenador2.list_pokemons[x].salud<=0:
                                                                    self.entrenador2.list_pokemons.remove(self.entrenador1.list_pokemons[x])
                                                                    print(f"el pokemon {self.entrenador1.pokemon1.nombre} de {self.entrenador2.nombre} gano la batalla")
                                                                    print(f"le quedan {self.entrenador1.pokemon1.salud} puntos de salud")
                                                                    print(f'{self.entrenador1.nombre} gano la batalla')
                                                                elif self.entrenador2.pokemon1.salud<=0:
                                                                    self.entrenador2.list_pokemons.remove(self.entrenador2.pokemon2)
                                                                    print(f"el pokemon {self.entrenador1.list_pokemons[x]} de {self.entrenador1.nombre} gano la batalla")
                                                                    print(f"le quedan {self.entrenador1.list_pokemons[x].salud} puntos de salud")
                                                                    print(f'{self.entrenador1.nombre} le queda solo un pokemon')
                                                else:pass
                                    elif self.entrenador2.pokemon1.salud<=0:
                                        pass
                            elif self.entrenador1.get_pokemon()==1:
                                pass

                        elif self.entrenador2.pokemon1.salud<=0:
                            self.entrenador2.list_pokemons.remove(self.entrenador2.pokemon1)
                            print(f"el pokemon {self.entrenador1.pokemon1.nombre} de {self.entrenador1} gano la batalla")
                            print(f"le quedan {self.entrenador1.pokemon1.salud} puntos de salud")
                            if self.entrenador2.get_pokemon()==0:
                                while self.entrenador2.list_pokemons[0].salud>0 and self.entrenador1.pokemon1.salud>0:
                                    self.entrenador2.list_pokemons[0].atacar(self.entrenador2.pokemon1)
                                    self.entrenador1.pokemon1.atacar(self.entrenador1.list_pokemons[0])
                                else:
                                    if self.entrenador2.list_pokemons[0].salud<=0:
                                        self.entrenador2.list_pokemons.remove(self.entrenador2.list_pokemons[0])
                                        print(f"el pokemon {self.entrenador1.pokemon1.nombre} de {self.entrenador2.nombre} gano la batalla")
                                        print(f"le quedan {self.entrenador1.pokemon1.salud} puntos de salud")
                                        print(f"A {self.entrenador2.nombre} solo le queda un pokemon")
                                        x=self.entrenador2.get_pokemon()
                                        while self.entrenador1.list_pokemons[x].salud>0 and self.entrenador2.pokemon1.salud>0:
                                            self.entrenador1.pokemon1.atacar(self.entrenador2.pokemon1)
                                            self.entrenador2.pokemon1.atacar(self.entrenador1.pokemon1)
                                        else:
                                            if self.entrenador2.pokemon1.salud<=0:
                                                self.entrenador2.list_pokemons.remove(self.entrenador2.list_pokemons[x])
                                                print(f"el pokemon {self.entrenador1.pokemon1.nombre} de {self.entrenador1.nombre} gano la batalla")
                                                print(f"le quedan {self.entrenador2.pokemon1.salud} puntos de salud")
                                                print(f'{self.entrenador2.nombre} gano el combate!!!')
                                            elif self.entrenador2.pokemon1.salud<=0:
                                                self.entrenador2.list_pokemons.remove(self.entrenador2.pokemon2)
                                                print(f"el pokemon {self.entrenador1.list_pokemons[0]} de {self.entrenador1.list_} gano la batalla")
                                                print(f"le quedan {self.entrenador1.list_pokemons[0].salud} puntos de salud")

                elif self.entrenador2.get_pokemon()==1:
                    pass
                else:
                    pass
            elif self.entrenador1.get_pokemon()==1:
                pass
            else:
                pass









combate=combate_pokemon(entrenador(coach1,"javi"),entrenador(coach2,"ruben"))
combate.comenzar()

