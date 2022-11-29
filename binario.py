# Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que
# introduzca un número binario e imprima por pantalla el número en formato decimal.
# Para desarrollar el programa, es necesario que desarrolles una función con la
# siguiente cabecera:
#
# def esBinario(strbinario)
# Devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado
# como parámetro contiene una cadena binaria.
# Ejemplo de esBinario:
# print(esBinario(“1001”))
# True
# print(esBinario(“Hola”))
# False

def binarioDecimal(strbinario):
    num_dec = 0

    for posicion, digito in enumerate(strbinario[::-1]):
        num_dec += int(digito) * 2 ** posicion

    print(f"La conversión del numero binario -> {strbinario} <- es: {num_dec}")
    return num_dec

def esBinario(strbinario):
    for numeros in strbinario:
        if((numeros == "0") or (numeros == "1")):
            print("El número introducido es binario")

            binarioDecimal(strbinario)
            return True
        else:
            print ("El número introducido no es binario")
            return False
        
unidad = input("Introduce un numero binario: ")
esBinario(unidad)
    