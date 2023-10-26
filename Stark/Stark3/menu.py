from data_stark import lista_personajes
from funciones import *

#Carnelos Duarte Joaquin Alejo 1B integrador 3


def stark_marvel_app(lista_personajes:list):
    global datos_normalizados  #llamamos a datos normalizados ya que cambia su comportamiento si fue llamada antes o si dio true
    while True:
        opcion = stark_menu_principal()
        if opcion is not False: #si ingrese una opcion valida arrancamos a operar
            match opcion:
                case 1:
                    stark_imprimir_nombres_con_iniciales_lista(lista_personajes)
                case 2:
                    stark_generar_codigos_heroes(lista_personajes)
                case 3:
                    stark_normalizar_datos(lista_personajes)
                case 4:
                    stark_imprimir_indice_nombre(lista_personajes)
                case 5:
                    stark_navegar_fichas(lista_personajes)
                case 6:
                    break #salimos del menu 
        else:
            print("Opción inválida. Ingresar uno de las opciones disponibles")

stark_marvel_app(lista_personajes)