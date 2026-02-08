import random

#Variables global del tablero
tablero = []


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
    return

def generar_tablero():
    """
    Crea el tablero con las filas y columnas numeradas
    inicialmente pone todas las casillas con un punto
    """
    return

def iniciar_partida():
    """
    Ajustamos todo para reiniciar una partida,
    en caso que haya terminado recien una
    """
    return


def buscar_coordenada():
    """
    Valida que la coordenada exista
    """
    return


def esta_revelada():
    """
    Verifica si la coordenada ya ha sido revelada
    """
    return

def es_mina():
    """
    Verifica si una coordenada corresponde a una mina
    """
    return

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
    return

def partida():
    """
    Mantiene el juego hasta que pierda o gane
    """
    return

def menu():
   """
    Opciones de inicio
    """
   return


menu() #ejecución