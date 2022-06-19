import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from random import choice

file=pd.read_csv('Pokemon2.csv',sep=",")
print(file.columns)
file=file[file["Legendary"]==False]
print(file.head())

file2=pd.DataFrame({"id":file["#"],"nombre":file["Name"],"ataque":file["Attack"],"defensa":file["Defense"],"salud":file["HP"]})
file2["ataque"]=file2["ataque"]/10
file2["defensa"]=file2["defensa"]/10
file2=file2[file2["salud"]<=100]
file2=file2[file2["ataque"]<=10]
file2=file2[file2["defensa"]<=10]
media_ataque=file2["ataque"].mean()
media_defensa=file2["defensa"].mean()
media_salud=file2["salud"].mean()
std_ataque=file2["ataque"].std()
std_defensa=file2["defensa"].std()
std_salud=file2["salud"].std()
file2=file2[file2["ataque"]<=(media_ataque+std_ataque)]
file2=file2[file2["defensa"]<=(media_defensa+std_defensa)]
file2=file2[file2["salud"]<=(media_salud+std_salud)]
file2=file2[file2["ataque"]>=(media_ataque-std_ataque)]
file2=file2[file2["defensa"]>=(media_defensa-std_defensa)]
file2=file2[file2["salud"]>=(media_salud-std_salud)]
file2=file2.drop_duplicates(subset=["id"])
file2=file2.dropna()
sns.boxplot(x="ataque",data=file2)
plt.show()
sns.boxplot(x="defensa",data=file2)
plt.show()
sns.boxplot(x="salud",data=file2)
plt.show()
file10=file2.to_csv("file2.csv")
class pokemon2:


    def __init__(self,id,nombre,salud,ataque,defensa,ids=list()):

        if id not in ids:
            self.id=id
            ids=ids.append(id)
        else:
            raise Exception("id ya registrado")
        if isinstance(nombre,str):
            self.nombre=nombre
        else:
            self.nombre="nombre"
        if 0<salud<=100:
            self.salud=salud
        else:
            raise Exception("salud erronea")
        if 0<ataque<=10:
            self.ataque=ataque
        else:
            raise Exception("ataque erroneo")
        if 0<defensa<=10:
            self.defensa=defensa
        else:
            raise Exception("defensa erronea")

    def descripcion(self):
        print(f'pokemon id {self.id}, with name {self.nombre} and health {self.salud}')

    def esta_vivo(self):
        if self.salud<=0:
            print("muerto")
        else:
            print(f'a {self.nombre} le quedan {self.salud} puntos de salud')
    def atacar(self,pokemon):
        if self.ataque > pokemon.defensa:
            if pokemon.salud>0:
                pokemon.salud = pokemon.salud - self.ataque
                print(True)
            else:
                print("el pokemon atacado ya esta muerto")
        else:
            print(False)
    def defender(self,daño):
        if daño<self.defensa:
            print(False)
        else:
            self.salud=self.salud-daño
            print(True)



pokemons_disponibles=[]
sep=","
archivo1="file2.csv"
with open(archivo1) as archivo:
    next(archivo)
    for linea in archivo:
        linea=linea.rstrip("/n")
        columnas=linea.split(sep)
        id=columnas[1]
        nombre=columnas[2]
        salud=columnas[5]
        ataque=columnas[3]
        defensa=columnas[4]
        pokemons_disponibles.append(pokemon2(id,nombre,float(salud),float(ataque),float(defensa)))


class entrenador_combate:
    def __init__(self,nombre,list_pokemons):
        if type(nombre)!= str:
            raise Exception("el nombre debe ser un string")
        else:
            self.nombre=nombre
        if type(list_pokemons)!= list:
            raise Exception("el grupo de pokemons, debe ser una lista")
        else:
            self.list_pokemons = list_pokemons

    def get_pokemon(self):
        print(f'{self.nombre} debe elegir uno de sus pokemons:')
        for i in range(0,len(self.list_pokemons)):
            print(f"\n{i}- {self.list_pokemons[i].nombre}")
        x=int(input())
        print(f'{self.nombre} eligio a {self.list_pokemons[x].nombre}')
        return int(x)

    def elegir_equipo(self):
        a=[]
        for i in range(0,3):
            x=self.get_pokemon()
            a.append(self.list_pokemons[x])
            self.list_pokemons.remove(self.list_pokemons[x])
        return a



class combate_pokemon:
    def __init__(self,entrenador1,entrenador2):
        self.entrenador1=entrenador1
        self.entrenador2=entrenador2
    def combate_individual(pokemon1,pokemon2):
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
        self.entrenador1.list_pokemons=self.entrenador1.elegir_equipo()
        self.entrenador2.list_pokemons=self.entrenador2.elegir_equipo()
        a=self.entrenador1.get_pokemon()
        b=self.entrenador2.get_pokemon()
        print("la batalla comienza en 3....,2....,1....")
        while self.entrenador1.list_pokemons!=[] and self.entrenador2.list_pokemons!=[]:
            combate_pokemon.combate_individual(self.entrenador1.list_pokemons[a],self.entrenador2.list_pokemons[b])
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


combate1=combate_pokemon(entrenador_combate("javi",pokemons_disponibles),entrenador_combate("ruben",pokemons_disponibles))
combate1.comenzar()


