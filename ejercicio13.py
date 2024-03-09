"""
EJERCICIO 13:    Comprobar palíndromos

Utilizar una pila para comprobar si una palabra o frase es un palíndromo

"""

class Pila:
    def __init__(self):
        self.items = []                                         # Inicializa una lista vacía para almacenar los elementos de la pila

    def esta_vacia(self):
        return self.items == []                                 # Devuelve True si la pila está vacía, False de lo contrario

    def apilar(self, item):
        self.items.append(item)                                 # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()                             # Elimina y devuelve el elemento en la parte superior de la pila

def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()                  # Elimina espacios en blanco y convierte la palabra a minúsculas
    pila = Pila()                                               # Crea una instancia de la clase Pila
    longitud = len(palabra)

    for i in range(longitud // 2):                              # Apila la primera mitad de los caracteres en la pila
        pila.apilar(palabra[i])

    if longitud % 2 != 0:                                       # Desplazarse a la mitad de la palabra si es impar
        i += 1

    while i < longitud:                                         # Compara los caracteres restantes con los desapilados de la pila
        if palabra[i] != pila.desapilar():
            return False
        i += 1
    return True

palabra = "reconocer"                                           # Palabra a verificar si es un palíndromo
if es_palindromo(palabra):                                      # Verifica si la palabra es un palíndromo
    print(f'"{palabra}" es un palíndromo.')                     # Imprime un mensaje si la palabra es un palíndromo
else:
    print(f'"{palabra}" no es un palíndromo.')                  # Imprime un mensaje si la palabra no es un palíndromo



"""
LA IMPRESIÓN FINAL SERÁ:

"reconocer" no es un palíndromo.

"""