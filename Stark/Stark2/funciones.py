from data_stark import lista_personajes
import sys
'''
1.0
'''
datos_numericos = {
        "fuerza": int,
        "altura": float,
        "peso": float,
        } #los datos a normalizar en el formato q deberían estar

datos_normalizados = False # creo la variable datos normalizados para futuros llamados

def stark_normalizar_datos(lista):
    global datos_normalizados # llamo a la global 
    bandera_error = False

    if datos_normalizados == True: #si ya se uso la funcion anterior
        print("Los datos ya han sido normalizados anteriormente.") 
        return False #deja de operar

    if not lista: #si la lista esta vacia o no se encuentra
        print("La lista está vacía.") 
        return False 

    for personaje in lista:
        for clave in datos_numericos:
            valor = personaje.get(clave) #saco el valor de la clave
            if valor != None: #si tiene alguno
                try: # intentar que
                    valor_normalizado = datos_numericos[clave](valor) # mi valor normalizado tiene que ser ser el valor de la clave
                    personaje[clave] = valor_normalizado #ese valor normalizado va a ser la clave de mi personaje
                except ValueError: #si hay un error
                    print(f"No se pudo normalizar {clave} en el personaje {personaje.get('nombre')}") # dejo constancia en la terminal de que clave es la que me molesta y que personaje es
                    bandera_error = True  # activo la bandera para indicar q hubo un error
            else: #si el valor estaba en blanco
                print(f"Falta el valor de {clave} en el personaje {personaje.get('nombre')}")
                bandera_error = True 

    if  bandera_error==False:  
        datos_normalizados = True  

    if datos_normalizados == True: 
        print("Datos Normalizados")
    else:
        print("No se ha podido normalizar, verifica que estén todos los datos en la lista")

    return datos_normalizados #retornamos los datos normalizados despues de todo el proceso anterior
'''
1.1
'''
def obtener_dato(heroe, clave):
    
    if clave in heroe:  #por si esta bien el diccionario, capaz lo escribo mal como por ejemplo "Fuersa"
        return heroe[clave] #retornamos el dato a buscar
    if not heroe:
        return False
'''
1.2
'''
def obtener_nombre(heroe):
    nombre = obtener_dato(heroe, "nombre")  #uso la funcion obtener dato con nombre como clave
    if nombre:
        return f"Nombre: {nombre}" #asi se vería el nombre formateado, ejemplo:   "Nombre: pipicucu"
    else:
        return False 
'''
2.0
'''
def obtener_nombre_y_dato(heroe, clave):
    if not lista_personajes: 
        print("La lista está vacía.")
        return False 

    if 0 <= heroe < len(lista_personajes): #cuenta los numeros de la lista, si el heroe esta dentro de su rango arranca la funcion
        nombre = obtener_nombre(lista_personajes[heroe])
        dato = obtener_dato(lista_personajes[heroe], clave)

        if dato is not None and nombre is not None: 
            return f"{nombre} | {clave}: {dato}"
        else:
            return f"No se pudo encontrar {clave} en el personaje {lista_personajes[heroe].get('nombre')}" # dejamos constancia del dato que falte
    return "El número del personaje excede el rango de la lista." # por si me piden el personaje n° x que supere el rango de la lista
'''
3.1
'''
def validar_numero(valor):
    try:
        numero = float(valor)  # Intentamos convertir el valor a un número flotante
        numero_redondeado = round(numero, 2)  # Redondeamos para futuros casos
        if numero_redondeado >= 0:  # verificamos que no sea negativo para futuras consignas
            return numero_redondeado
        else:
            return False
    except (ValueError, TypeError):#si no pudo convertise en float
        return False

def obtener_maximo(lista, key):
    if not lista:
        return False 
    
    maximo = float('-inf') #el minimo valor posible, siempre va a ser superado por cualquier numero
    for x in lista: 
        valor = x.get(key) #sacamos su valor, ejemplo "fuerza: 123"; tomamos el 123
        if validar_numero(valor): 
            valor = validar_numero(valor)  
            if valor >= maximo: 
                maximo = valor
        else:
            return False # si no supero la validación entonces retornara false
    return maximo 

'''
3.2
'''

def obtener_minimo(lista, key):
    if not lista:
        return False
    minimo = float('inf')
    for x in lista:
        valor = x.get(key)
        if validar_numero(valor):
            valor = validar_numero(valor)  
            if valor <= minimo:
                minimo = valor
        else:
            return False 
    return minimo 
#igual que la funcion obtener maximo pero invertido
'''
3.3
'''
def obtener_dato_cantidad(lista, X, clave): 
    lista_condicion = []
    X = float(X)  #en el segundo parametro se busca que lo represente a un float
    for heroe in lista:
        if clave in heroe:
            heroe_X = heroe.get(clave)
            if heroe_X is not None: # aca no me dejaba usar != así que tuve que usar not
                heroe_X = float(heroe_X) #el valor tiene que ser un float
                if heroe_X == X:   #si hay coincidencia
                    lista_condicion.append(heroe)
    return lista_condicion 

'''
3.4
'''
def stark_imprimir_heroes(lista): #imprime  cada nombre de los objetos de la lista
    if not lista:
        return False
    for heroe in lista: 
            print(f"{heroe.get('nombre')}")
'''
4.1
'''
def sumar_dato_heroe(lista, clave):
    contador = 0
    
    for heroe in lista:
        if isinstance(heroe, dict):#si tal diccionario esta bien estructurado
            valor = heroe.get(clave)
            if validar_numero(valor):  # Verificar que valor sea un número
                contador += valor  # Sumar el valor redondeado al contador
            else:
                print(f"Valor no válido en {clave}: {heroe.get(clave)}")#dejamos constancia de donde hay un error
                return False
    return contador

'''
4.2
'''
def dividir(dividendo, divisor):
    dividendo_valido = validar_numero(dividendo)
    divisor_valido = validar_numero(divisor)
    
    if dividendo_valido is not False and divisor_valido is not False and divisor_valido != 0: #solo sin is not me daba el resultado distinto a false
        resultado = round(dividendo_valido / divisor_valido, 2)  
        return resultado
    else:
        return False

'''
4.3
'''
def calcular_promedio(lista, clave):
    suma = sumar_dato_heroe(lista, clave)
    cantidad = len(lista)

    if cantidad == 0:
        return False
    else:
        promedio = dividir(suma, cantidad)
        return promedio
'''
4.4
'''
def mostrar_promedio_dato(lista, clave):
    if not lista:
        print("La lista está vacía.")
        return False

    promedio = calcular_promedio(lista, clave)
    if promedio is not False:
        print(f"El promedio de {clave} es: {promedio:.2f}")
        return promedio
    else:
        return False
'''
5.1
'''
def imprimir_menu():
    print("Menú de opciones:")
    print("1. Normalizar datos (No se puede poder acceder a los otras opciones, sin normalizar antes)")
    print("2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB")
    print("3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M")
    print("6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB")
    print("7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB")
    print("8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("10. Listar todos los superhéroes agrupados por color de ojos.")
    print("11. Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("12. Salir")
'''
5.2
'''
def validar_entero(numero):
    if numero.isdigit():
        return True
    else:
        return False
'''
5.3
'''
def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese el número de una opción: ")
    
    if validar_entero(opcion):
        return int(opcion)
    else:
        return False
'''
menu
'''
def obtener_superheroes_por_genero(lista_personajes: list, genero: str):
    if not lista_personajes:
        return False

    superheroes_por_genero = []
    heroes_con_problemas = []

    for i, heroe in enumerate(lista_personajes): #buscamos por cada heroe, el i es para luego buscar la dirección del caso en el falle
        heroe_genero = heroe.get("genero")

        if heroe_genero is not None and isinstance(heroe_genero, str) and heroe_genero.strip():# si el genero esta escrito, en cadena y no esta en blanco
            if heroe_genero == genero:
                superheroes_por_genero.append(heroe)
        else: #en el caso que falle vamos a tener aca donde esta el error
            nombre_heroe = heroe.get("nombre", f"Héroe {i + 1}") 
            heroes_con_problemas.append(nombre_heroe)

    if heroes_con_problemas:
        print(f"Esta mal escrito o directamente esta ausente el genero de:{heroes_con_problemas}")
        return False

    return superheroes_por_genero


'''
menu ojos
'''
def diccionarios_por_ojos(lista_personajes: list): #funciona igual que la anterior solo que enfocada en los ojos
    if not lista_personajes:
        return False

    diccionario_color_ojos = {}
    heroes_con_problemas = []

    for i, heroe in enumerate(lista_personajes):
        color_ojos = heroe.get("color_ojos")
        if color_ojos is not None and isinstance(color_ojos, str) and color_ojos.strip():
            if color_ojos not in diccionario_color_ojos:
                diccionario_color_ojos[color_ojos] = 0
            diccionario_color_ojos[color_ojos] += 1
        else:
            nombre_heroe = heroe.get("nombre", f"Héroe {i + 1}")
            heroes_con_problemas.append(nombre_heroe)

    if heroes_con_problemas:
        print("Esta mal escrito o directamente esta ausente el color de ojos de:")
        return heroes_con_problemas
    else:
        return diccionario_color_ojos


def imprimir_cantidad_por_color_de_ojos(lista_personajes: list):

    print(diccionarios_por_ojos(lista_personajes))

def listar_personajes_por_color_ojos(lista_personajes: list):
    diccionario_color_ojos = diccionarios_por_ojos(lista_personajes)

    for color_ojos, heroe in diccionario_color_ojos.items():   #bucle donde buscamos todos los colores de ojos en el diccionario y los diferenciamos
        print(f"Personajes con color de ojos '{color_ojos}':")
        for heroe in lista_personajes:
            if heroe.get("color_ojos") == color_ojos:
                print(f"- {heroe['nombre']}")
'''
menu pelo
'''
def diccionarios_por_pelo(lista_personajes: list):
    if not lista_personajes:
        return False

    diccionarios_por_pelo = {}
    heroes_con_problemas = []

    for i, heroe in enumerate(lista_personajes):
        color_pelo = heroe.get("color_pelo")
        if color_pelo is not None and isinstance(color_pelo, str) and color_pelo.strip():
            if color_pelo not in diccionarios_por_pelo:
                diccionarios_por_pelo[color_pelo] = 0
            diccionarios_por_pelo[color_pelo] += 1
        else:
            nombre_heroe = heroe.get("nombre", f"Héroe {i + 1}")
            heroes_con_problemas.append(nombre_heroe)

    if heroes_con_problemas:
        print("Esta mal escrito o directamente está ausente el color de pelo de:")
        return heroes_con_problemas
    else:
        return diccionarios_por_pelo

def imprimir_cantidad_por_color_de_pelo(lista_personajes: list):

    print(diccionarios_por_pelo(lista_personajes))
'''
menu inteligencia
'''
def diccionarios_por_inteligencia(lista_personajes: list):
    if not lista_personajes:
        return {}

    diccionarios_por_inteligencia = {}
    heroes_con_problemas = []

    for i, heroe in enumerate(lista_personajes):
        inteligencia = heroe.get("inteligencia")
        if inteligencia is not None and isinstance(inteligencia, str) and inteligencia.strip():
            if inteligencia not in diccionarios_por_inteligencia:
                diccionarios_por_inteligencia[inteligencia] = 0
            diccionarios_por_inteligencia[inteligencia] += 1
        else:
            nombre_heroe = heroe.get("nombre", f"Héroe {i + 1}")
            heroes_con_problemas.append(nombre_heroe)

    if heroes_con_problemas:
        print("Esta mal escrito o directamente está ausente la inteligencia de:")
        for heroe_con_problema in heroes_con_problemas:
            print(heroe_con_problema)
        return {} #si no fuera por estas llaves se rompe la funcion en caso de error

    return diccionarios_por_inteligencia

def listar_personajes_por_inteligencia(lista_personajes: list):
    diccionario_inteligencia = diccionarios_por_inteligencia(lista_personajes)  # Cambia el nombre de la variable

    for inteligencia, heroe in diccionario_inteligencia.items():  # Cambia el nombre de la variable
        print(f"Personajes con inteligencia '{inteligencia}':")
        for heroe in lista_personajes:
            if heroe.get("inteligencia") == inteligencia:
                print(f"- {heroe['nombre']}")

'''
5.4
'''
#era mas facil hacer estas listas fuera del stark_marvel_app que andar poniendo muchas veces el mismo 
lista_masculina = obtener_superheroes_por_genero(lista_personajes, 'M')
lista_femenina = obtener_superheroes_por_genero(lista_personajes, 'F')
lista_nb = obtener_superheroes_por_genero(lista_personajes, 'NB')

def stark_marvel_app(lista_personajes):
    global datos_normalizados #llamamos a la global de los datos como en el primer punto
    bandera_while = True
    while bandera_while:
        opcion = stark_menu_principal()
        if opcion is not False: # llamamos a la funcion del menu principal y si no dio False, proseguimos
            if opcion == 1:
                stark_normalizar_datos(lista_personajes)
            elif datos_normalizados==True:  #sin los datos, nada de lo siguiente se puede realizar
                if opcion == 2:
                    stark_imprimir_heroes(lista_nb)
                elif opcion == 3:
                    mas_alta = obtener_maximo(lista_femenina, "altura")
                    obtener_nombre_mas_alta = obtener_dato_cantidad(lista_femenina, mas_alta, "altura")
                    stark_imprimir_heroes(obtener_nombre_mas_alta)
                elif opcion == 4:
                    mas_alto = obtener_maximo(lista_masculina, "altura")
                    obtener_nombre_mas_alta = obtener_dato_cantidad(lista_masculina, mas_alto, "altura")
                    stark_imprimir_heroes(obtener_nombre_mas_alta)
                elif opcion == 5:
                    mas_debil = obtener_minimo(lista_masculina,"fuerza")
                    obtener_nombre_mas_debil = obtener_dato_cantidad(lista_masculina, mas_debil, "fuerza")
                    stark_imprimir_heroes(obtener_nombre_mas_debil)
                elif opcion == 6:
                    mas_debil_nb = obtener_minimo(lista_nb,"fuerza")
                    obtener_nombre_mas_debil_nb = obtener_dato_cantidad(lista_nb, mas_debil_nb, "fuerza")
                    stark_imprimir_heroes(obtener_nombre_mas_debil_nb)
                elif opcion == 7:
                    mostrar_promedio_dato(lista_nb,"fuerza")
                elif opcion == 8:
                    imprimir_cantidad_por_color_de_ojos(lista_personajes)
                elif opcion == 9:
                    imprimir_cantidad_por_color_de_pelo(lista_personajes) #en data stark esta en blanco el pelo de groot, la variable anda si le pones algun valor como "no hair", no se si hay que modificarlo
                elif opcion == 10:
                    listar_personajes_por_color_ojos(lista_personajes)
                elif opcion == 11:
                    listar_personajes_por_inteligencia(lista_personajes)# al igual que groot con su "" en pelo, calculo que el espacio vacio del pato es por su elevada inteligencia pero como no tiene valor alguno, lo marco como error
            elif opcion == 12:
                sys.exit()
            else:
                print("Primero hay que normalizar los datos(opción 1 del menú).")