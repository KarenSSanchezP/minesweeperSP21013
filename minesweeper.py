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

def iniciar_partida(dimension, num_minas):
    """
    Ajustamos todo para reiniciar una partida,
    en caso que haya terminado recien una
    """
    # Variables globales para el tablero y las minas
    global tablero
    global matriz_minas
    
    tablero = generar_tablero(dimension) # generamos el tablero
    matriz_minas = generar_minas(dimension, num_minas) # generamos las minas
    
    imprimir_tablero() # imprimimos el tablero
    
    return


def traducir_coordenada(coordenada):
    """
    Traduce una coordenada de la forma A1 a 0,0 
    para poder usarla en la matriz del tablero
    """
    letra = coordenada[0]
    numero = int(coordenada[1:])
    
    fila = ord(letra) - 65 # convertimos la letra a un numero (A=0, B=1, etc.)
    columna = numero - 1 # convertimos el numero a un indice de columna (1=0, 2=1, etc.)
    
    return fila, columna


def esta_revelada(coordenada):
    """
    Verifica si la coordenada ya ha sido revelada
    """
    fila, columna = traducir_coordenada(coordenada) # traducimos la coordenada a indices de fila y columna
    
    if tablero[fila][columna] != ".": # verificamos si la casilla ya ha sido revelada (si no es un punto)
        return True
    return False

def es_mina(coordenada):
    """
    Verifica si una coordenada corresponde a una mina
    """
    fila, columna = traducir_coordenada(coordenada) # traducimos la coordenada a indices de fila y columna
    
    if matriz_minas[fila][columna]: # verificamos si hay una mina en esa coordenada
        return True
    else:
        return False

def vecinos(fila, columna):
    """
    Recopila todos los vecinos de una casilla,
    verificando que no invente vecinos,
    osea que no vaya a crear casillas fuera del tablero
    (si la casilla esta en la orilla por ejemplo)
    """
    lista_vecinos = [] # lista de vecinos
    
    # Recorremos cada casilla del tablero que rodea a la casilla dada
    for i in range(-1, 2):
        for j in range(-1, 2):
            vecino_fila = fila + i # calculamos la fila del vecino
            vecino_columna = columna + j # calculamos la columna del vecino
            
            if i == 0 and j == 0: # si es la misma casilla, no se agrega
                continue
            
            # Validamos que la coordenada del vecino sea válida
            if not (0 <= vecino_fila < len(tablero) and 0 <= vecino_columna < len(tablero[0])):
                continue
            
            tupla_vecino = (vecino_fila, vecino_columna) # guardamos la coordenada del vecino
            lista_vecinos.append(tupla_vecino) # agregamos la coordenada al listado de vecinos
    
    return lista_vecinos

def contar_minas(fila, columna):
    """
    Cuenta el numero de minas alrededor de una casilla
    """
    minas_cercanas = 0 # contador de minas cercanas
    mis_vecinos = vecinos(fila, columna) # obtenemos la lista de vecinos de la casilla dada
    
    for vecino in mis_vecinos: # recorremos cada vecino
        fila_vecino, columna_vecino = vecino # extraemos la coordenada del vecino
        
        if matriz_minas[fila_vecino][columna_vecino]: # si el vecino es una mina, sumamos 1
            minas_cercanas += 1
    return minas_cercanas

def desplazar_mina(coordenada):
    """
    Si es el primer movimiento
    mueve la mina a otra casilla
    """
    if es_mina(coordenada):
        fila, columna = traducir_coordenada(coordenada)
        matriz_minas[fila][columna] = False # cambiamos la mina a False
        
        # Obtenemos la lista de vecinos de la casilla
        vecinos_a_desplazar = vecinos(fila, columna)
        
        # Recorremos cada vecino y lo desplazamos
        for vecino in vecinos_a_desplazar:
            fila_vecino, columna_vecino = vecino
            if matriz_minas[fila_vecino][columna_vecino] == False: # cambiamos el vecino a 
                matriz_minas[fila_vecino][columna_vecino] = True
                break # una vez que desplazamos la mina, salimos del bucle
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
    fila, columna = traducir_coordenada(coordenada)
    pendientes = [(fila, columna)] # pila de casillas pendientes por revelar
    
    while pendientes:
        fila, columna = pendientes.pop() # sacamos la casilla de la pila
        
        if tablero[fila][columna] != ".": # si ya se ha revelado, no se muestra
            continue 
        
        if matriz_minas[fila][columna]: # si es una mina, no se muestra
            continue 
        
        minas_cercanas = contar_minas(fila, columna) # contamos las minas cercanas
        
        if minas_cercanas > 0: # mostramos el número de minas cercanas
            tablero[fila][columna] = str(minas_cercanas) 
        elif minas_cercanas == 0: # si no hay minas cercanas, agregamos los vecinos a la pila
            vecinos_a_revelar = vecinos(fila, columna) # obtenemos la lista de vecinos de la casilla
            tablero[fila][columna] = " " # cambiamos el contenido 
            
            for vecino in vecinos_a_revelar: # recorremos cada vecino
                fila_vecino, columna_vecino = vecino
                # si el vecino no ha sido revelado, lo agregamos a la pila
                if tablero[fila_vecino][columna_vecino] == ".":
                    pendientes.append((fila_vecino, columna_vecino))
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
    mensaje_error = "" # variable para almacenar el mensaje de error, si es necesario
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # limpiamos la pantalla para que se vea mejor    

        imprimir_tablero() # imprimimos el tablero
        
        if mensaje_error:
            print(mensaje_error) # imprimimos el mensaje de error si existe
            mensaje_error = "" # reseteamos el mensaje de error para la siguiente iteración
        
        coord = input("Ingrese una coordenada, sin espacios (ej.: A1): ").upper() # pedimos la coordenada
        
        # Validación de formato y longitud
        if len(coord) < 2 or len(coord) > 3 or not (coord[0].isalpha() and coord[1:].isdigit()):
            mensaje_error = "Coordenada inválida. Intente de nuevo"
            time.sleep(1)
            continue
        
        # Extraemos la letra y el número de la coordenada
        letra = coord[0]
        numero = int(coord[1:])
        
        limite_letras = chr(64 + len(tablero)) # letra máxima permitida según el tamaño del tablero
        
        # Validación de rango. Debería ser A-P y 1-16
        if not ('A' <= letra <= limite_letras and 1 <= numero <= len(tablero)):
            mensaje_error = "Coordenada fuera de rango. Intente de nuevo"
            time.sleep(1)
            continue
        
        # Validación de que la coordenada no exista
        if esta_revelada(coord):
            mensaje_error = "La casilla ya ha sido revelada. Intente de nuevo"
            time.sleep(1)
            continue
    return coord

def partida(opcion):
    """
    Mantiene el juego hasta que pierda o gane
    """
    
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