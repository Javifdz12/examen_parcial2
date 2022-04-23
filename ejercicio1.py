class pokemon:
    def __init__(self,id,nombre,arma,salud,ataque,defensa):
        if isinstance(id,int):
            self.id=id
        else:
            print("holi")
        self.nombre=nombre
        self.arma=arma
        self.salud=salud
        self.ataque=ataque
        self.defensa=defensa
