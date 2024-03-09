"""
EJERCICIO 6:  Invertir una cadena

Utilizar una pila para invertir el orden de los caracteres de una cadena

"""


class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

def invertir_cadena(cadena):
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)

    cadena_invertida = ''
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()

    return cadena_invertida

# Ejemplo de uso
cadena_original = "Hola mundo!"
cadena_invertida = invertir_cadena(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)
