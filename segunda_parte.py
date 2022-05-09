import pandas as pd
import seaborn as sns

file=pd.read_csv('Pokemon2.csv',sep=",")
print(file.columns)
file=file[file["Legendary"]==False]
print(file.head())

file2=pd.DataFrame({"id":file["#"],"nombre":file["Name"],"ataque":file["Attack"],"defensa":file["Defense"],"salud":file["HP"]})
file2["ataque"]=file2["ataque"]/10
file2["defensa"]=file2["defensa"]/10
file2=file2[file2["ataque"]<=10]
file2=file2[file2["defensa"]<=10]
file2=file2.to_csv("file2.csv")

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
        if 1<salud<100:
            self.salud=salud
        else:
            raise Exception("salud erronea")
        if 1<=ataque<=10:
            self.ataque=ataque
        else:
            raise Exception("ataque erroneo")
        if 1<=defensa<=10:
            self.defensa=defensa
        else:
            raise Exception("defensa erronea")

    def descripcion(self):
        print(f'pokemon id {self.id}, with name {self.nombre}, has a weapon {self.arma} and health {self.salud}')

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
x=3
pokemons_grupos_de_3=lambda pokemons_disponibles:[pokemons_disponibles[i:i+x] for i in range(0,len(pokemons_disponibles))]
print(pokemons_grupos_de_3)
class entrenador_combate:
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