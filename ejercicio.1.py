"""
EJERCICIO 1:  Duplicar Nodos

Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista duplicada hacia adelante y hacia atrás

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
            self.inicio = self.fin = nuevo_nodo
            
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def duplicar_nodos(self):
        actual = self.inicio
        while actual:
            nuevo_nodo = NodoDoble(actual.dato)
            siguiente_nodo = actual.siguiente
            nuevo_nodo.siguiente = siguiente_nodo
            nuevo_nodo.anterior = actual
            actual.siguiente = nuevo_nodo
            if siguiente_nodo:
                siguiente_nodo.anterior = nuevo_nodo
            actual = siguiente_nodo

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
lista_original = ListaEnlazadaDoble()
lista_original.insertar_al_final(1)
lista_original.insertar_al_final(2)
lista_original.insertar_al_final(3)
lista_original.insertar_al_final(4)

# Duplicar nodos
lista_original.duplicar_nodos()

print("Lista original hacia adelante:")
lista_original.imprimir_adelante()

print("\nLista original hacia atrás:")
lista_original.imprimir_atras()

