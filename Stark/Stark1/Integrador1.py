from data_stark import lista_personajes
from funciones import*
import sys

bandera_while= True
while bandera_while == True:
    opcion = input("\nA.Imprimir datos de cada superhéroe\nB.Identidad y el peso del superhéroe con mayor fuerza\nC. Nombre e identidad del superhéroe más bajo\nD. Peso promedio de los superhéroes masculinos\nE. Nombre y peso de superhéroes que superen la fuerza promedio femenina\nF. Salir\n")
    match opcion.upper():  # con upper me deja usar en la terminal tanto mayuscula como minuscula
        case "A":
            for personaje in lista_personajes:#Recorro cada miembro de la lista
                    nombre = personaje["nombre"]
                    identidad = personaje["identidad"]
                    empresa = personaje["empresa"]
                    altura = float(personaje["altura"])
                    peso = float(personaje["peso"])
                    genero = personaje["genero"]
                    color_ojos = personaje["color_ojos"]
                    color_pelo = personaje["color_pelo"]
                    fuerza = int(personaje["fuerza"])
                    inteligencia = personaje["inteligencia"] #cargo cada una de sus categorias
                    print(f'{nombre}\t{identidad}\t{empresa}\t{altura}cm\t{peso}kg\t{genero}\t{color_ojos}\t{color_pelo}\t{fuerza}\t{inteligencia}\n')
                    #imprimo a cada miembro con f'' , {} para llamar lo q necesito, \t para poner un espacio y \n para hacer un salto de renglon
        
        case "B":
            fuerzas = [int(personaje["fuerza"]) for personaje in lista_personajes] #Busco la Fuerza de cada personaje en esta constante
            mayor_fuerza = encontrar_mayor(fuerzas) # utilizo las fuerzas como x en mi funcion y logro encontrar el maximo
            super_heroes_fuertes = []
            
            for personaje in lista_personajes: #hago este primer bucle para encontrar a los personajes mas fuertes
                if int(personaje['fuerza']) == mayor_fuerza:   #si la fuerza es = a la mayor
                    super_heroes_fuertes.append(personaje) #sumo a ese personaje a la lista
            
            
            for personaje in super_heroes_fuertes: #llamo a los personajes mas fuertes marcados y obtengo sus datos
                nombre = personaje["nombre"]
                identidad = personaje["identidad"]
                peso = float(personaje["peso"])
                print(f"{nombre} - Identidad: {identidad} - Peso: {peso:0.2f} kg") 
        
        case "C":
            altura = [float(personaje["altura"]) for personaje in lista_personajes] #Busco la altura de cada personaje  en esta constante
            menor_altura = encontrar_menor(altura) # utilizo las alturas como x en mi funcion y logro encontrar el minimo
            super_hereos_bajitos = []
            
            for personaje in lista_personajes:  #hago este primer bucle para encontrar a los personajes mas bajitos
                if float(personaje['altura']) == menor_altura:
                    super_hereos_bajitos.append(personaje) #sumo a ese personaje a la lista}

            for personaje in super_hereos_bajitos: # llamo a los personajes mas bajitos marcados y obtengo sus datos
                nombre = personaje["nombre"]
                identidad = personaje["identidad"]
                altura = float(personaje["altura"])
                print(f"{nombre} - Identidad: {identidad}, Altura: {altura:.2f} cm")
        
        case "D":
            peso_acumulado_masculinos = [float(personaje["peso"]) for personaje in lista_personajes if personaje["genero"] == "M"]
            #en esta constante busco el peso de cada personaje y le agrego la condición de que sea de genero masculino
            promedio_masculino = calcular_promedio(peso_acumulado_masculinos) # y luego facilmente uso la constante de peso como X en la funcion de promedio
            print(f"El peso promedio de los superhéroes masculinos es de {promedio_masculino:0.2f} kg.")# y listo imprimo lo que obtuve en la linea anterior
        
        case "E":
            fuerza_acumulada_femenina = [int(personaje["fuerza"]) for personaje in lista_personajes if personaje["genero"] == "F"]
            #como en el caso anterior, solo que aca busco la fuerza de cada personaje de genero femenino
            fuerza_promedio_femenina = calcular_promedio(fuerza_acumulada_femenina)
            # y luego facilmente uso la constante de fuerza como X en la funcion de promedio
            for personaje in lista_personajes: #recorro la lista
                fuerza = int(personaje["fuerza"])#pido la fuerza
                if fuerza> fuerza_promedio_femenina:# y si es mayor como pide el caso, doy los datos de los que lo cumplan
                    peso = float(personaje["peso"])
                    nombre = personaje["nombre"]
                    print(f"{nombre} , {peso} kg")
       
        case "F":
            sys.exit()