"""
EJERCICIO 4:  Eliminar Nodos Duplicados

Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás

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

    def eliminar_duplicados(self):
        datos_vistos = set()
        actual = self.cabeza
        previo = None
        while actual:
            if actual.dato in datos_vistos:
                previo.siguiente = actual.siguiente
                del actual
                actual = previo.siguiente
            else:
                datos_vistos.add(actual.dato)
                previo = actual
                actual = actual.siguiente

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

# Crear la lista enlazada con datos duplicados
lista = ListaEnlazada()
datos = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
for dato in datos:
    lista.insertar(dato)

# Eliminar nodos duplicados
lista.eliminar_duplicados()

# Imprimir la lista hacia adelante y hacia atrás
print("Lista sin nodos duplicados hacia adelante:")
lista.imprimir_adelante()
print("Lista sin nodos duplicados hacia atrás:")
lista.imprimir_atras()
