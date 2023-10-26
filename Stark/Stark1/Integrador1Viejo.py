from data_stark import lista_personajes
import sys
bandera_while= True

while bandera_while == True:
    opcion = input("\nA.Imprimir datos de cada superhéroe\nB.Identidad y el peso del superhéroe con mayor fuerza\nC. Nombre e identidad del superhéroe más bajo\nD. Peso promedio de los superhéroes masculinos\nE. Nombre y peso de superhéroes que superen la fuerza promedio femenina\nF. Salir\n")
    match opcion.upper():  # Convertir a mayúsculas para comparar sin importar la capitalización
        case "A":
            for personaje in lista_personajes:
                    nombre = personaje["nombre"]
                    identidad = personaje["identidad"]
                    empresa = personaje["empresa"]
                    altura = float(personaje["altura"])
                    peso = float(personaje["peso"])
                    genero = personaje["genero"]
                    color_ojos = personaje["color_ojos"]
                    color_pelo = personaje["color_pelo"]
                    fuerza = int(personaje["fuerza"])
                    inteligencia = personaje["inteligencia"]
                    print(f'{nombre}\t{identidad}\t{empresa}\t{altura}cm\t{peso}kg\t{genero}\t{color_ojos}\t{color_pelo}\t{fuerza}\t{inteligencia}\n')
        case "B":
            banderaFuerza = False
            fuerzaMayor=0
            superHeroesFuertes = []
            for personaje in lista_personajes:
                fuerza = int(personaje["fuerza"])
                if banderaFuerza== False or fuerzaMayor<fuerza:
                    banderaFuerza = True
                    fuerzaMayor = fuerza
                    superHeroesFuertes = [personaje]
                elif fuerza == fuerzaMayor:
                    superHeroesFuertes.append(personaje)
            if superHeroesFuertes!= None:
                if len(superHeroesFuertes) == 1:
                    print(f"El superhéroe con mayo fuerza es")
                else:
                    print(f"Los superhéroes con mayo fuerza son")
                for personaje in superHeroesFuertes:
                    nombre = personaje["nombre"]
                    identidad = personaje["identidad"]
                    peso = float(personaje["peso"])
                    print(f"{nombre}       Identidad: {identidad}    Peso: {peso:0.2f} kg")
        case "C":
            alturaMin = float('inf')
            banderaBaja = 0
            superHerosMasBajos = []
            for personaje in lista_personajes:
                altura = float(personaje["altura"])
                if banderaBaja==0 or alturaMin>altura:
                    banderaBaja=1
                    alturaMin=altura
                    superHerosMasBajos = [personaje]
                elif alturaMin == altura:
                    superHerosMasBajos.append(personaje)
            if superHerosMasBajos!=None:
                if len(superHerosMasBajos) == 1:
                    print("El superhéroe más bajo es:")
                else:
                    print("Los superhéroes más bajos son:")
                for personaje in superHerosMasBajos:
                    nombre = personaje["nombre"]
                    identidad = personaje["identidad"]
                    altura = float(personaje["altura"])
                    print(f"{nombre} - Identidad: {identidad}, Altura: {altura:.2f} cm")
        case "D":
            acumuladorPesoM = 0
            contadorM=0
            for personaje in lista_personajes:
                genero = personaje["genero"]
                if genero == "M":
                    peso = float(personaje["peso"])
                    acumuladorPesoM+=peso
                    contadorM+=1
            promedioPesoM= acumuladorPesoM/contadorM
            print(F"El peso promedio de los superhéroes masculinos es de {promedioPesoM:0.2f} kg.")
        case "E":
            contadorFemenino= 0
            fuerzaSumaFemenina= 0
            for personaje in lista_personajes:
                genero = personaje["genero"]
                fuerza = int(personaje["fuerza"])
                if genero == "F":
                    contadorFemenino+=1
                    fuerzaSumaFemenina+= fuerza
            fuerzaPromedioF= fuerzaSumaFemenina/contadorFemenino
            for personaje in lista_personajes:
                fuerza = int(personaje["fuerza"])
                if fuerza> fuerzaPromedioF:
                    peso = float(personaje["peso"])
                    nombre = personaje["nombre"]
                    print(f"{nombre} , {peso} kg\n")
        case "F":
            sys.exit()