from data_stark import lista_personajes
import re

#Carnelos Duarte Joaquin Alejo 1B integrador 3
'''
1.1
'''
def extraer_iniciales(nombre_heroe: str)-> str:
    if not nombre_heroe: #en caso de espacio vacio
        return 'N/A'
    if not isinstance(nombre_heroe, str): #en caso de que el parametro no sea un string
        return False 
    
    nombre_heroe = re.sub(r'-', ' ', nombre_heroe) # remplazar guion con espacio en blanco
   
    nombre_heroe = re.sub(r'\bthe\b', '', nombre_heroe, flags=re.IGNORECASE) #igual que la anterior solo que aca se filtra para borra la inicial "the", tomando \b como inicial

    iniciales = '.'.join(re.findall(r'\b\w', nombre_heroe.upper())) #buscamos cada resultado, lo separamos le metemos el . y que revise bien con el r'\b\w'
    iniciales += '.'  #lo necestiaba para el punto final
    return iniciales
'''
1.2
'''
def obtener_dato_formato(dato: str)-> str:

    if not isinstance(dato, str):#validamos string
        return False
    else:
        dato = dato.lower() #formateamos a minuscula
        dato = re.sub(r'[^a-zA-Z0-9]', '_', dato)#sub reemplaza los datos, dentro del sub hay 3 paramateros, 1) los permitidos 2)si no esta permitido se reemplaza por el segundo parametro '_' 3) la variable a la cual vamos a formatear
        return dato
'''
1.3
'''
def stark_imprimir_nombre_con_iniciales(nombre_heroe: dict) -> str:
    if not isinstance(nombre_heroe, dict):  # Validamos que el parámetro sea un diccionario
        return "El parámetro no es un diccionario."
    
    nombre = nombre_heroe.get('nombre', '')  
    if not nombre:
        return "* N/A" #aca validamos que el diccionario tenga la clave nombre, como no lo tiene retornamos este formato para futuros usos

    iniciales = extraer_iniciales(nombre)
    nombre_formato = obtener_dato_formato(nombre)

    return f"* {nombre_formato} ({iniciales})" #solo logre que funcione así, con un return TRUE me devuelve true en la terminal a todo
'''
1.4
'''
def stark_imprimir_nombres_con_iniciales_lista(lista_heroes: list):
    if not isinstance(lista_heroes, list): #validamos que el parametro sea una lista
        print("El parametro no es una lista.")
        return False
    
    if not lista_heroes: #validamos que tenga al menos un elemento
        print("La lista está vacía.")
        return False

    for heroe in lista_heroes:
        resultado = stark_imprimir_nombre_con_iniciales(heroe)
        print(resultado)

        if not resultado:
            return False
    return True
'''
2.1
'''
def generar_codigo_heroe(diccionario_heroe: dict, id_heroe: int) -> str:
    try:
        if not isinstance(diccionario_heroe, dict): 
            raise ValueError #validacion de q el parametro sea un diccionario
        genero = diccionario_heroe.get('genero', '')
        if genero not in ('M', 'F', 'NB'):
            raise ValueError #validamos de que los generos sean estos y que exista la clave

        primer_numero = {'M': '1', 'F': '2', 'NB': '0'}.get(genero) #asignamos un numero a cada genero validado
        ceros = 10 - (len(genero) + len(primer_numero) + 1) 
        #en total necesitamos 10 caracteres, así que los ceros seran el rdo. de la resta entre (10 y la suma de los len del genero, numero y 1(el caracter que ocupa el guion))
        id_heroe_str = str(id_heroe).zfill(ceros) #transformamos a string, cada id que se genera automaticamente, y con zfil agregamos los ceros a su izquierda
        codigo_heroe = f'{genero}-{primer_numero}{id_heroe_str}'

        return codigo_heroe
    except (ValueError):
        return 'N/A'
'''
2.2
'''
def stark_generar_codigos_heroes(lista_heroes: list):
    try:
        if not lista_heroes or not all(isinstance(heroe, dict) for heroe in lista_heroes):
            raise ValueError("La lista de héroes es inválida o está vacía.")
        #Validamos que La lista contenga al menos un elemento 
        #usamos el all(insistance) para todos los elementos que esten dentro de la lista gracias al for
        codigos = [] #mi cadena
        for i, heroe in enumerate(lista_heroes, start=1): 
        #start es una variable  dentro de python que se usa en la funcion enumerate para arrancar desde el N° asignado. En cada i(elemento) arrancamos a contar
            formato = stark_imprimir_nombre_con_iniciales(heroe)
            codigo = generar_codigo_heroe(heroe, i)
            codigos.append(f"{formato} | {codigo}")

        mensaje_codigos = ("\n".join(codigos))
        cantidad_codigos = len(codigos)

        if cantidad_codigos == 1:
            mensaje_final = "Se asignó 1 código"
        else:
            mensaje_final = f"Se asignaron {cantidad_codigos} códigos"

        print(f"{mensaje_codigos}\n{mensaje_final}")
        return True
    
    except ValueError as ex:
        print(str(ex))
        return False
'''
3.1
'''
def sanitizar_entero(numero_str: str)-> int:

    numero_str = numero_str.strip() #borramos todos el espacio en blanco en la cadena

    
    if not numero_str.isdigit(): #Si contiene carácteres no numéricos retornar -1
        return -1 
    
    try:
        numero_entero = int(numero_str) #lo convertimos a entero
        if numero_entero < 0: #para numero negativos
            return -2
        else: #en caso contrario (positivos y el 0), lo retornamos en int
            return numero_entero
    except: #errores que escapen a lo pensado
        return -3
'''
3.2
'''
def sanitizar_flotante(numero_str: str)-> float: #igual que la anterior solo que con floats

    numero_str = numero_str.strip()

    try:
        # Intentar convertir el string a un número de punto flotante
        numero_flotante = float(numero_str)
        if numero_flotante < 0:
            return -2  
        else:
            numero_flotante = round(numero_flotante, 2)
            return numero_flotante
    except ValueError:
        return -1  # con value error logro que me retorne -1 en caso de que alguno no sea digito ya que isdigit parece romperse con los floats
    except:
        return -3  # errores  que escapan a lo anterior
'''
3.3 
'''
def sanitizar_string(valor_str: str,  valor_por_defecto='-') -> str:
    try:
        valor_str = valor_str.strip() #sacamos los espacios en blanco previos
        valor_str = valor_str.replace('/', ' ') #en caso de una barra, la reemplazamos por un espacio en blanco que si validamos
        
        if any(caracter.isdigit() for caracter in valor_str): # bucle en busqueda de al menos un digito 
            return "N/A"
        
        if not valor_str:  # Si el string esta vacio lo cambiamos por el defecto
            valor_str = valor_por_defecto
        
        return valor_str.lower() #al final lo pasamos a minuscula
    except: #en caso de alguna excepción que escape a lo definido anteriormente retornamos n/a tambien
        return "N/A"
'''
3.4 
'''
def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str):
    tipo_dato = tipo_dato.lower() #transformando a minuscula logramos que sea el que sea el parametro no haya confusion

    if tipo_dato not in ('string', 'entero', 'flotante'): # en el tercer parametro siempre va a dar False algo fuera de estas opciones
        print("Tipo de dato no reconocido")
        return False
    
    if clave not in heroe:  #por si directamente falta la clave, ejemplo un diccionario sin fuerza
        print("La clave especificada no existe en el héroe")
        return False
    
    valor = heroe[clave] #conseguimos el valor asignado a cada clave en los diccionarios 
    

    match tipo_dato: #match del tercer parametro
        case 'string':
            resultado = sanitizar_string(str(valor)) #aplicamos la funcion correspondiente, el valor tiene que ser string
        case 'entero':
            resultado = sanitizar_entero(str(valor))
        case 'flotante':
            resultado = sanitizar_flotante(str(valor))

    if resultado is not None and resultado not in (-1, -2, -3,"N/A"): # si resultado existe y es distinto a estos valores
        heroe[clave] = resultado #lo retornamos
        return True 
    else: #caso contrarios
        return False
'''
3.5 
'''
datos_normalizados = False #creo mi global

def stark_normalizar_datos(lista: list) -> bool: #mi booleano final dependera de la global
    global datos_normalizados # la llamo

    if datos_normalizados == True: #si ya normalizamos anteriormente
        print("Los datos ya han sido normalizados anteriormente.")
        return False

    bandera_error = False

    transformar_claves = {'altura': 'flotante', 'peso': 'flotante', 'color_ojos': 'string', 'color_pelo': 'string', 'fuerza': 'entero', 'inteligencia': 'string'}
    #creo diccionario con las claves y su tipo de dato correspondiente

    if not lista:
        print("Error: Lista de héroes vacía")
        return False

    if not isinstance(lista, list):
        print("El parámetro no es una lista.")
        return False

    for personaje in lista: # por personaje en la lista
        for clave, tipo_dato in transformar_claves.items(): #con items logro que mi diccionario se divida en 2, primero la clave va a ser la de la izquierda del : y luego tipo de dato va a ser su correspondiente en otro tupla
            if clave not in personaje: # si falta la clave me dira donde
                print(f"Falta el valor de {clave} en el personaje {personaje.get('nombre')}")
                bandera_error = True
            else: #caso contrario arrancamos

                valor = personaje[clave]
                
                if clave in ['color_ojos', 'color_pelo', 'inteligencia']:
                        personaje[clave] = re.sub(r'^\s*$', 'No tiene', personaje[clave]) #remplazamos el espacio en blanco por un no tiene
                         #tuve que sacarlo del try porque sino no cambiaba los valores
                        
                if not isinstance(valor, str):
                    bandera_error = True

                try:
                    sanitizar_dato(personaje, clave, tipo_dato)#usamos lo generado en la linea  for clave, tipo_dato in transformar_claves.items() para la funcion sanitizar_dato
                    
                    if not sanitizar_dato(personaje, clave, tipo_dato):# si fallo la sanitazión tiene que dar el error
                        print(f"No se pudo sanitizar el dato {clave} en el personaje {personaje.get('nombre')}") 
                        bandera_error = True

                except:
                    print(f"No se pudo sanitizar el dato {clave} en el personaje {personaje.get('nombre')}")
                    bandera_error = True 

    if not bandera_error: # si no hubo ningun error
        datos_normalizados = True
        print("Datos Normalizados")
    else: 
        print("No se ha podido normalizar, verifica que estén todos los datos en la lista")
        datos_normalizados = False

    return datos_normalizados
'''
4.1 
'''
def stark_imprimir_indice_nombre(lista_heroes: list):
    nombres_formateados = []
    for heroe in lista_heroes:
        nombre = heroe.get('nombre', '') 
        nombre = re.sub(r'\bthe\b', '', nombre.lower())  #devuelta sacamos el the
        nombre = re.sub(r'\s+', '-', nombre)  # '\s+' busca donde se repita de forma consecutiva el siguiente parametro, y se lo remplaza por 1
        nombres_formateados.append(nombre)
    
    indice_cadena = '-'.join(nombres_formateados) #separamos por guion cada nombre
    print(indice_cadena)

'''
5.1
'''
def generar_separador(patron, largo, imprimir= True)-> str:

    if not (1 <= largo <= 235) or not (1 <= len(patron) <= 2): #si el largo excede el patron o si ponen un patron que no sea 1/2 caracteres
        return 'N/A'
    
    separador = patron * largo
    
    if imprimir: #si es true como en el parametro original se imprime doble, si lo ponen como false va  a ser solo una linea
        print(separador)
    
    return separador
'''
5.2
'''
def generar_encabezado(titulo:str)-> str:
    titulo = titulo.upper()
    separador = generar_separador('**',75, imprimir= False)
    encabezado = print(f"{separador}\n{titulo}\n{separador}")
    return encabezado
'''
5.3
'''
def imprimir_ficha_heroe(heroe: dict):
    principal = generar_encabezado("Principal")

    nombre_iniciales = stark_imprimir_nombre_con_iniciales(heroe)
    nombre_iniciales = nombre_iniciales.replace('*', '') #en la consigna los nombres aparcen sin asterisco así q los sacamos

    identidad = heroe.get('identidad', '')
    imprimir_identidad = obtener_dato_formato(identidad)

    consultora = heroe.get('empresa', '')
    imprimir_consultora = obtener_dato_formato(consultora)

    id_heroe = lista_personajes.index(heroe) + 1 # con index arrancamos a contar cada numero del diccionario(le sumamos 1 para q arranque a contar en 1 y no en 0)
    codigo = generar_codigo_heroe(heroe, id_heroe)

    uno = f"{principal}\nNOMBRE DEL HÉROE:\t{nombre_iniciales}\nIDENTIDAD SECRETA:\t{imprimir_identidad}\nCONSULTORA:\t{imprimir_consultora}\nCÓDIGO DE HÉROE:\t{codigo}"

    fisico = generar_encabezado("Físico")
    altura = heroe.get('altura', '')
    peso = heroe.get('peso', '')
    fuerza = heroe.get('fuerza', '')

    dos = f"\nALTURA:\t{altura} cm.\nPESO:\t{peso} kg.\nFUERZA:\t{fuerza} N"

    señas = generar_encabezado("Señas Particulares")
    color_ojos = heroe.get('color_ojos', '')
    color_pelo = heroe.get('color_pelo', '')

    tres = f"\nCOLOR DE OJOS:\t{color_ojos}\nCOLOR DE PELO:\t{color_pelo}"

    #ni separandolo en 3 cuerpos logre que los encabezados esten en el orden que pide la consigna

    ficha = f"{uno}\n{fisico}\n{dos}\n{señas}\n{tres}\n"
    ficha = re.sub(r'None', '', ficha) # me salia un none así que directamente lo filtre al final
    print(ficha)
    return ficha
    #no logre que se vean los separadores en orden en la terminal ni como ajustar las columnas
'''
5.4
'''
def stark_navegar_fichas(lista_heroes):
    if not isinstance(lista_heroes, list):  # Validar que el parámetro sea una lista
        print("El parámetro no es una lista.")
        return
    
    if not lista_heroes:
        print("La lista de héroes está vacía")
        return

    total_lista = len(lista_heroes)
    actual = 0 #así logramos que imprima el primero de la lista

    while True:
        imprimir_ficha_heroe(lista_heroes[actual])
        print("[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ 3 ] Salir")
        opcion = input("Ingrese opción: ")

        match opcion:
            case '1':
                actual = (actual - 1) % total_lista #con % total lista, logramos que actual se mueva dentro de los valores de la lista, no podría dar 20 si solo hay 3 opciones
            case '2':
                actual = (actual + 1) % total_lista
            case '3':
                break
            case _:
                print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
'''
6.0
'''
def imprimir_menu():
    print("Menú de opciones:")
    print("1 - Imprimir la lista de nombres junto con sus iniciales")
    print("2 - Imprimir la lista de nombres y el código del mismo")
    print("3 - Normalizar datos")
    print("4 - Imprimir índice de nombres")
    print("5 - Navegar fichas")
    print("6 - Salir")


def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese el número de una opción: ")
    
    if opcion.isdigit() and 1 <= int(opcion) <= 6:  #solo tomamos digitos, que esten entre 1 y 6
        return int(opcion)#solo tomamos enteros
    else:
        return False