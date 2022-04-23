from enum import Enum
class armas(Enum):
    puñetazo=2
    patada=4
    codazo=3
    cabezazo=5
class pokemon:

    def __init__(self,id,nombre,arma,salud,ataque,defensa):
        ids=[]
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
    def __del__(self):
        #ids=ids.remove(self.id)
        print(f'pokemon {self.nombre} fue eliminado de la lista')


pokemon1=pokemon(1,2,armas.puñetazo,50,4,5)
pokemon2=pokemon(3,"pikachu",armas.patada,67,10,5)
pokemon3=pokemon(5,"charmander",armas.cabezazo,58,6,4)
pokemon3.descripcion()
pokemon2.descripcion()
del pokemon1
pokemon4=pokemon(2,"pepe",armas.puñetazo,50,4,5)