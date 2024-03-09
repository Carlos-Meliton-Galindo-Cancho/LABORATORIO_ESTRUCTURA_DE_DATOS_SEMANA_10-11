"""
EJERCICIO 3:  Insertar Nodo en Posición Específica

Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la lista hacia adelante y hacia atrás

"""


class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def insertar_al_final(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.inicio is None:
            self.inicio = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def insertar_en_posicion(self, dato, posicion):
        nuevo_nodo = NodoDoble(dato)
        if posicion == 1:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            for _ in range(1, posicion - 1):
                actual = actual.siguiente
            siguiente_nodo = actual.siguiente
            nuevo_nodo.siguiente = siguiente_nodo
            nuevo_nodo.anterior = actual
            actual.siguiente = nuevo_nodo
            if siguiente_nodo:
                siguiente_nodo.anterior = nuevo_nodo
            else:
                self.fin = nuevo_nodo

    def imprimir_adelante(self):
        actual = self.inicio
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def imprimir_atras(self):
        actual = self.fin
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.anterior
        print("None")

# Crear lista original
lista = ListaEnlazadaDoble()
lista.insertar_al_final(1)
lista.insertar_al_final(2)
lista.insertar_al_final(3)
lista.insertar_al_final(4)
lista.insertar_al_final(5)

# Insertar nodo en posición 3 con dato 15
lista.insertar_en_posicion(15, 3)

print("Lista hacia adelante:")
lista.imprimir_adelante()

print("\nLista hacia atrás:")
lista.imprimir_atras()


































