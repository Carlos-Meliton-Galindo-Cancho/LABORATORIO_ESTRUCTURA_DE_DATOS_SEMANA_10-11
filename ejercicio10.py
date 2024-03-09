"""
EJERCICIO 10:   Ordenar una pila

Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales

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

    def cima(self):
        return self.items[-1]

    def tamano(self):
        return len(self.items)


def ordenar_pila_ascendente(pila):
    pila_auxiliar = Pila()

    while not pila.esta_vacia():
        elemento = pila.desapilar()

        while not pila_auxiliar.esta_vacia() and pila_auxiliar.cima() > elemento:
            pila.apilar(pila_auxiliar.desapilar())

        pila_auxiliar.apilar(elemento)

    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

# Ejemplo de uso
pila = Pila()
elementos = [3, 1, 4, 1, 5, 9, 2, 6, 5]
for elemento in elementos:
    pila.apilar(elemento)

print("Pila original:", pila.items)

ordenar_pila_ascendente(pila)

print("Pila ordenada ascendente:", pila.items)
