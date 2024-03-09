"""
EJERCICIO 11:   Eliminar duplicados

Eliminar los elementos duplicados de una pila

"""



class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]

    def tamano(self):
        return len(self.items)

def eliminar_duplicados(pila):
    # Crear un conjunto para almacenar elementos únicos
    elementos_unicos = set()
    # Crear una pila auxiliar para almacenar elementos no duplicados
    pila_auxiliar = Pila()

    # Desapilar los elementos de la pila original y agregarlos a la pila auxiliar si no están en el conjunto de elementos únicos
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in elementos_unicos:
            elementos_unicos.add(elemento)
            pila_auxiliar.apilar(elemento)

    # Desapilar los elementos de la pila auxiliar y volver a apilarlos en la pila original
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

# Ejemplo de uso
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(2)
pila.apilar(4)
pila.apilar(3)

print("Pila original:", pila.items)

eliminar_duplicados(pila)

print("Pila sin duplicados:", pila.items)














