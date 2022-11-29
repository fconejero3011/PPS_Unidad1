# Realiza, utilizando Python 3, el ejercicio 3 de la página 35 del libro “Introducción a
# Python” de Jon Vadillo e inclúyelo en un fichero llamado lista.py. Las funciones que
# debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes
# cabeceras:
#
# def estaEnRango(valor, minimo, maximo)
# Devuelve True o False determinando que valor se encuentra entre el mínimo y el
# máximo.
# def estaEnLista(valor, lista)
# Devuelve True o False determinando si el valor está en la lista.

def estaEnRango(numero, min, max):
    if numero > max:
        print("Has introducido un numero mayor al intervalo especificado anteriormente")
        return False
    elif numero < min:
        print("Has introducido un numero menor al intervalo especificado anteriormente")
        return False
    else:
        print("Has introducido un numero cadecuado al intervalo especificado anteriormente")
        return True

def estaEnLista(numero, lista):

    find = 0

    for numeros in lista:
        if numero == numeros:
            find = 1
    if find == 1:
        print("El numero está en lista")
        return True
    else:
        print("El numero no esta en lista")
        return False
    
numero = int(input("Introduzca un numero entre 1 y 20: "))
min = 1
max = 20

estaEnRango(numero, min, max)

lista = [5, 14, 11, 3, 2, 1, 15, 19]

valor = int(input("Introduzca el numero de nuevo: "))
estaEnLista(valor, lista)