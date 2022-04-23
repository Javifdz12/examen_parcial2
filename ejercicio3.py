from ejercicio1 import pokemon
pokemons_coach1=[]
sep=","
archivo1="coach_1_pokemons.csv"
with open(archivo1) as archivo:
    next(archivo)
    for linea in archivo:
        linea=linea.rstrip("/n")
        columnas=linea.split(sep)
        id=columnas[0]
        nombre=columnas[1]
        arma=columnas[2]
        salud=columnas[3]
        ataque=columnas[4]
        defensa=columnas[5]
        pokemons_coach1.append(pokemon(id,nombre,arma,int(salud),int(ataque),int(defensa)))

pokemons_coach2=[]
sep=","
archivo2="coach_2_pokemons.csv"
with open(archivo2) as archivo:
    next(archivo)
    for linea in archivo:
        linea=linea.rstrip("/n")
        columnas=linea.split(sep)
        id=columnas[0]
        nombre=columnas[1]
        arma=columnas[2]
        salud=columnas[3]
        ataque=columnas[4]
        defensa=columnas[5]
        pokemons_coach1.append(pokemon(id,nombre,arma,int(salud),int(ataque),int(defensa)))
