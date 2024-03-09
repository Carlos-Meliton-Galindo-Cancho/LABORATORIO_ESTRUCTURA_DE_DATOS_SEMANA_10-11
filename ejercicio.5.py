"""
EJERCICIO 5:  Invertir la Lista

Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el primero y viceversa e imprime la lista hacia adelante y hacia atrás

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

    def invertir_lista(self):
        actual = self.inicio
        while actual:
            siguiente_temp = actual.siguiente
            actual.siguiente = actual.anterior
            actual.anterior = siguiente_temp
            actual = siguiente_temp
        # Cambiar inicio y fin
        self.inicio, self.fin = self.fin, self.inicio

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
for i in range(1, 7):
    lista.insertar_al_final(i)

# Invertir la lista
lista.invertir_lista()

print("Lista invertida hacia adelante:")
lista.imprimir_adelante()

print("\nLista invertida hacia atrás:")
lista.imprimir_atras()
