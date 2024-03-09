"""
EJERCICIO 6:  Invertir una cadena

Utilizar una pila para invertir el orden de los caracteres de una cadena

"""


class Pila:
    def __init__(self):
        self.items = []                                                   # Inicializa una lista vacía para almacenar los elementos de la pila

    def esta_vacia(self):
        return self.items == []                                           # Verifica si la pila está vacía

    def apilar(self, item):
        self.items.append(item)                                           # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        return self.items.pop()                                           # Elimina y devuelve el elemento en la parte superior de la pila

def invertir_cadena(cadena):
    pila = Pila()                                                         # Crea una instancia de la clase Pila para almacenar los caracteres de la cadena
    for caracter in cadena:
        pila.apilar(caracter)                                             # Apila cada caracter de la cadena en la pila en el orden original

    cadena_invertida = ''                                                 # Inicializa una cadena vacía para almacenar la cadena invertida
    while not pila.esta_vacia():                                          # Mientras la pila no esté vacía
        cadena_invertida += pila.desapilar()                              # Desapila cada caracter de la pila y lo agrega al inicio de la cadena invertida

    return cadena_invertida                                               # Devuelve la cadena invertida

cadena_original = "Hola mundo!"                                           # Cadena original
cadena_invertida = invertir_cadena(cadena_original)                       # Invierte la cadena original
print("Cadena original:", cadena_original)                                # Imprime la cadena original
print("Cadena invertida:", cadena_invertida)                              # Imprime la cadena invertida



"""
LA IMPRESIÓN FINAL SERÁ:

Cadena original: Hola mundo!
Cadena invertida: !odnum aloH

"""