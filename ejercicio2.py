from enum import Enum
import random
class armas(Enum):
    puñetazo=2
    patada=4
    codazo=3
    cabezazo=5
class pokemon_tierra:


    def __init__(self,id,nombre,arma,salud,ataque,defensa,ids=list()):

        if id not in ids:
            self.id=id
            ids=ids.append(id)
        else:
            raise Exception("id ya registrado")
        if isinstance(nombre,str):
            self.nombre=nombre
        else:
            self.nombre="nombre"
        self.arma=arma
        if 1<salud<100:
            self.salud=salud
        else:
            raise Exception("salud erronea")
        if 1<=ataque<=10:
            self.ataque=ataque
        else:
            raise Exception("ataque erroneo")
        if 11<=defensa<=20:
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

class pokemon_agua:


    def __init__(self,id,nombre,arma,salud,ataque,defensa,ids=list()):

        if id not in ids:
            self.id=id
            ids=ids.append(id)
        else:
            raise Exception("id ya registrado")
        if isinstance(nombre,str):
            self.nombre=nombre
        else:
            self.nombre="nombre"
        self.arma=arma
        if 1<salud<100:
            self.salud=salud
        else:
            raise Exception("salud erronea")
        if 11<=ataque<=20:
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

class pokemon_aire:


    def __init__(self,id,nombre,arma,salud,ataque,defensa,ids=list()):

        if id not in ids:
            self.id=id
            ids=ids.append(id)
        else:
            raise Exception("id ya registrado")
        if isinstance(nombre,str):
            self.nombre=nombre
        else:
            self.nombre="nombre"
        self.arma=arma
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
            if random.choice([True,False])==True:
                self.salud=self.salud-daño
                print(True)
            else:
                print(False)
                print(f'{self.nombre} esquivo el ataque')

class pokemon_electricidad:


    def __init__(self,id,nombre,arma,salud,ataque,defensa,ids=list()):

        if id not in ids:
            self.id=id
            ids=ids.append(id)
        else:
            raise Exception("id ya registrado")
        if isinstance(nombre,str):
            self.nombre=nombre
        else:
            self.nombre="nombre"
        self.arma=arma
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
            if random.choice([True,False])==True:
                if pokemon.salud>0:
                    self.ataque=self.ataque*2
                    pokemon.salud = pokemon.salud - self.ataque
                    print(True)
                    print(f'el ataque de {self.nombre} fue muy potente')
                else:
                    print("el pokemon atacado ya esta muerto")
            else:
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

pokemon1=pokemon_tierra(1,2,armas.puñetazo,50,3,14)
pokemon2=pokemon_electricidad(3,"pikachu",armas.patada,67,10,5)
pokemon3=pokemon_aire(5,"charmander",armas.cabezazo,58,6,4)
pokemon2.atacar(pokemon3)
pokemon3.esta_vivo()
pokemon3.defender(10)
pokemon3.esta_vivo()
pokemon2.atacar(pokemon1)
