"""
EJERCICIO 10:   Ordenar una pila

Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales

"""


class Pila:
    def __init__(self):
        self.items = []                                                             # Inicializa una lista vacía para almacenar los elementos de la pila

    def esta_vacia(self):
        return self.items == []                                                     # Verifica si la pila está vacía

    def apilar(self, item):
        self.items.append(item)                                                     # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        return self.items.pop()                                                     # Elimina y devuelve el elemento en la parte superior de la pila

    def cima(self):
        return self.items[-1]                                                       # Devuelve el elemento en la cima de la pila

    def tamano(self):
        return len(self.items)                                                      # Devuelve el número de elementos en la pila

def ordenar_pila_ascendente(pila):
    pila_auxiliar = Pila()                                                          # Crea una pila auxiliar para almacenar los elementos temporalmente

    while not pila.esta_vacia():                                                    # Mientras la pila original no esté vacía
        elemento = pila.desapilar()                                                 # Desapila el elemento superior de la pila original

        while not pila_auxiliar.esta_vacia() and pila_auxiliar.cima() > elemento:   # Mueve los elementos mayores que el elemento desapilado a la pila auxiliar
            pila.apilar(pila_auxiliar.desapilar())                                  # Desapila y vuelve a apilar en la pila original
 
        pila_auxiliar.apilar(elemento)                                              # Apila el elemento desapilado en la pila auxiliar

    while not pila_auxiliar.esta_vacia():                                           # Una vez que la pila original esté vacía, todos los elementos estarán en la pila auxiliar en orden ascendente
        pila.apilar(pila_auxiliar.desapilar())                                      # Se vuelven a apilar en la pila original en orden ascendente

pila = Pila()                                                                       # Crea una instancia de la clase Pila
elementos = [3, 1, 4, 1, 5, 9, 2, 6, 5]                                             # Lista de elementos para la pila
for elemento in elementos:
    pila.apilar(elemento)                                                           # Apila cada elemento en la pila

print("Pila original:", pila.items)                                                 # Imprime la pila original

ordenar_pila_ascendente(pila)                                                       # Ordena la pila ascendente

print("Pila ordenada ascendente:", pila.items)                                      # Imprime la pila ordenada ascendentemente



"""
LA IMPRESIÓN FINAL SERÁ:

Pila original: [3, 1, 4, 1, 5, 9, 2, 6, 5]
Pila ordenada ascendente: [9, 6, 5, 5, 4, 3, 2, 1, 1]

"""