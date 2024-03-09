"""
EJERCICIO 11:   Eliminar duplicados

Eliminar los elementos duplicados de una pila

"""


class Pila:
    def __init__(self):
        self.items = []                                            # Inicializa una lista vacía para almacenar los elementos de la pila

    def esta_vacia(self):
        return self.items == []                                    # Verifica si la pila está vacía

    def apilar(self, item):
        self.items.append(item)                                    # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        if not self.esta_vacia():                                  # Verifica si la pila no está vacía antes de desapilar
            return self.items.pop()                                # Elimina y devuelve el elemento en la parte superior de la pila

    def cima(self):
        if not self.esta_vacia():                                  # Verifica si la pila no está vacía
            return self.items[-1]                                  # Devuelve el elemento en la cima de la pila

    def tamano(self):
        return len(self.items)                                     # Devuelve el número de elementos en la pila

def eliminar_duplicados(pila):
    elementos_unicos = set()                                       # Crea un conjunto para almacenar elementos únicos
    pila_auxiliar = Pila()                                         # Crea una pila auxiliar para almacenar elementos no duplicados

    while not pila.esta_vacia():                                   # Desapila los elementos de la pila original y los agrega a la pila auxiliar si no están en el conjunto de elementos únicos
        elemento = pila.desapilar()                                # Desapila un elemento de la pila original
        if elemento not in elementos_unicos:                       # Verifica si el elemento no está en el conjunto de elementos únicos
            elementos_unicos.add(elemento)                         # Agrega el elemento al conjunto de elementos únicos
            pila_auxiliar.apilar(elemento)                         # Apila el elemento en la pila auxiliar

    while not pila_auxiliar.esta_vacia():                          # Desapila los elementos de la pila auxiliar y los vuelve a apilar en la pila original
        pila.apilar(pila_auxiliar.desapilar())                     # Desapila un elemento de la pila auxiliar y lo apila en la pila original

pila = Pila()                                                      # Crea una instancia de la clase Pila
pila.apilar(1)  
pila.apilar(2)
pila.apilar(3)                                                     # Apila varios elementos en la pila original
pila.apilar(2)
pila.apilar(4)
pila.apilar(3)

print("Pila original:", pila.items)                                # Imprime la pila original

eliminar_duplicados(pila)                                          # Llama a la función para eliminar los elementos duplicados de la pila

print("Pila sin duplicados:", pila.items)                          # Imprime la pila sin elementos duplicados



"""
LA IMPRESIÓN FINAL SERÁ:

Pila original: [1, 2, 3, 2, 4, 3]
Pila sin duplicados: [1, 2, 4, 3]

"""

