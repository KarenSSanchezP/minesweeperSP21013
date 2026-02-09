import random
import os
import time

#Variables global del tablero
tablero = [] # matriz del tablero


def generar_minas(filas_cols, num_minas):
    """
    Función para generar el tablero con las minas
    """
    global minas
    minas = [True] * num_minas + [False] * (filas_cols **2 - num_minas)
    random.shuffle(minas)
    return [minas[i:i+filas_cols] for i in range(0, len(minas), filas_cols)]

def imprimir_tablero():
    """
    Imprime el tablero, 
    lo convierte de matriz a algo entendible para el usuario
    """
    letras = [chr(65+i) for i in range(len(tablero))] # lista de letras para identificar las filas
    numeros = list(range(1, len(tablero)+1)) # lista de numeros para identificar las columnas
    
    for i in range(len(numeros)): # imprimimos la numeracion de las columnas
        print(" " if numeros[i] < 10 else "", numeros[i], end="") # imprimimos el numero de la fila
    print() # salto de linea
    for i in range(len(tablero)): # imprimimos la identificacion de las filas y el contenido del tablero
        print(letras[i], end=" ")
        for j in range(len(tablero[i])):
            print(tablero[i][j], end="  ")
        print()
    return tablero

def generar_tablero(filas_cols):
    """
    Crea el tablero con las filas y columnas numeradas
    inicialmente pone todas las casillas con un punto
    """
    tablero_temp = [] # matriz del tablero temporal
    for i in range(filas_cols): 
        tablero_temp.append([]) # se agrega una nueva fila
        for j in range(filas_cols): 
            tablero_temp[i].append(".") # se agrega una nueva columna
    return tablero_temp

def iniciar_partida():
    """
    Ajustamos todo para reiniciar una partida,
    en caso que haya terminado recien una
    """
    global tablero
    tablero = generar_tablero(16) # generamos el tablero
    imprimir_tablero() # imprimimos el tablero
    return


def buscar_coordenada():
    """
    Valida que la coordenada exista
    """
    return


def esta_revelada(coordenada):
    """
    Verifica si la coordenada ya ha sido revelada
    """
    if coordenada in tablero:
        return True
    else:
        return False

def es_mina(coordenada):
    """
    Verifica si una coordenada corresponde a una mina
    """
    if coordenada in minas:
        return True
    else:
        return False

def vecinos():
    """
    Recopila todos los vecinos de una casilla,
    verificando que no invente vecinos,
    osea que no vaya a crear casillas fuera del tablero
    (si la casilla esta en la orilla por ejemplo)
    """
    return

def contar_minas():
    """
    Cuenta el numero de minas alrededor de una casilla
    """
    return

def desplazar_mina():
    """
    Si es el primer movimiento
    mueve la mina a otra casilla
    """
    return


def mostrar_contenido(coordenada):
    """
    Muestra el contenido de la casilla,
    si tiene minas cercanas solo el valor de cuantas minas hay,
    sino crea una reaccion en cadena.

    (Para el segundo caso)
    Podemos simular una pila para esta reaccion en cadena
    e ir añadiendo los vecinos hasta que no hayan más
    valores libres en el perímetro
    """
    return

def mostrar_minas():
    """
    Muestra todas las minas de un tablero
    en caso de perder o terminar la partida
    """
    return


def revelar_coordenada(coordenada):
    """
    Verifica si es una mina,
    si lo es, muestra todas las minas
    sino muestra el contenido de la coordenada
    """
    return

def pedir_coordenada():
    """
    Pide una coordenada al usuario
    """
    coordenada = input("Coordenada: ")
    if not (len(coordenada) == 2 and coordenada[0].isalpha() and coordenada[1].isdigit()):
        print("Coordenada inválida")
        return pedir_coordenada()
    if esta_revelada(coordenada):
        print("La casilla ya ha sido revelada")
    elif es_mina(coordenada):
        print("La casilla es una mina")
    return coordenada

def partida(opcion):
    """
    Mantiene el juego hasta que pierda o gane
    """
    while True:
        coordenada = pedir_coordenada()
        if esta_revelada(coordenada):
            print("La casilla ya ha sido revelada")
        elif es_mina(coordenada):
            print("La casilla es una mina")
        else:
            print("La casilla no es una mina")
        
        if es_mina(coordenada):
            mostrar_minas()
        else:
            mostrar_contenido(coordenada)
    return

def menu():
    """
    Opciones de inicio
    """
    
    # Limpiamos la pantalla para que se vea mejor el menu
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Imprimimos el menú
    print("--- Bienvenido al juego del Buscaminas ---\n"+ "-"*42)
    print("\nElija un modo de juego\n" + 
        "1. Normal \n2. Avanzado \n3. Salir")
    
    opcion = input("Opcion: ")
    if opcion == "1":
        partida(opcion)
    elif opcion == "2":
        partida(opcion)
    elif opcion == "3":
        print("Gracias por jugar")
        time.sleep(1)
        return
    else:
        print("Opcion invalida")
        time.sleep(2)
        menu()
    return


#menu() #ejecución
iniciar_partida()