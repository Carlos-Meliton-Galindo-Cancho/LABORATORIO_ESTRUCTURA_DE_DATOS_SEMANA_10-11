"""
EJERCICIO 2:  Contar Nodos Pares e Impares

Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato impar e imprime la lista hacia adelante y hacia atrás

"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def contar_pares_impares(self):
        actual = self.cabeza
        pares = 0
        impares = 0
        while actual:
            if actual.dato % 2 == 0:
                pares += 1
            else:
                impares += 1
            actual = actual.siguiente
        return pares, impares

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def imprimir_atras(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo:
            self.imprimir_atras(nodo.siguiente)
            print(nodo.dato, end=" -> ")

# Crear la lista enlazada
lista = ListaEnlazada()
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for dato in datos:
    lista.insertar(dato)

# Contar nodos pares e impares
pares, impares = lista.contar_pares_impares()
print("Cantidad de nodos pares:", pares)
print("Cantidad de nodos impares:", impares)

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
lista.imprimir_adelante()
print("Lista hacia atrás:")
lista.imprimir_atras()
