"""
EJERCICIO 3:  Insertar Nodo en Posición Específica

Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la lista hacia adelante y hacia atrás

"""


class NodoDoble:
    def __init__(self, dato):
        self.dato = dato                                             # Almacena el dato del nodo
        self.siguiente = None                                        # Inicializa el enlace al siguiente nodo como None
        self.anterior = None                                         # Inicializa el enlace al nodo anterior como None

class ListaEnlazadaDoble:
    def __init__(self):
        self.inicio = None                                           # Inicializa el primer nodo de la lista como None
        self.fin = None                                              # Inicializa el último nodo de la lista como None

    def insertar_al_final(self, dato):
        nuevo_nodo = NodoDoble(dato)                                 # Crea un nuevo nodo con el dato dado
        if self.inicio is None:                                      # Verifica si la lista está vacía
            self.inicio = nuevo_nodo                                 # Si la lista está vacía, el nuevo nodo se convierte en el primer y último nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin                           # El enlace anterior del nuevo nodo apunta al nodo que actualmente es el último
            self.fin.siguiente = nuevo_nodo                          # El enlace siguiente del nodo que actualmente es el último apunta al nuevo nodo
            self.fin = nuevo_nodo                                    # El nuevo nodo se convierte en el último nodo de la lista

    def insertar_en_posicion(self, dato, posicion):
        nuevo_nodo = NodoDoble(dato)                                 # Crea un nuevo nodo con el dato dado
        if posicion == 1:                                            # Verifica si la posición es la primera
            nuevo_nodo.siguiente = self.inicio                       # El enlace siguiente del nuevo nodo apunta al nodo que era inicialmente el primero
            self.inicio.anterior = nuevo_nodo                        # El enlace anterior del nodo que era inicialmente el primero apunta al nuevo nodo
            self.inicio = nuevo_nodo                                 # El nuevo nodo se convierte en el primer nodo de la lista
        else:
            actual = self.inicio
            for _ in range(1, posicion - 1):                         # Avanza en la lista hasta la posición anterior a la deseada
                actual = actual.siguiente
            siguiente_nodo = actual.siguiente                        # Guarda una referencia al nodo siguiente al nodo actual
            nuevo_nodo.siguiente = siguiente_nodo                    # El enlace siguiente del nuevo nodo apunta al nodo siguiente al nodo actual
            nuevo_nodo.anterior = actual                             # El enlace anterior del nuevo nodo apunta al nodo actual
            actual.siguiente = nuevo_nodo                            # El enlace siguiente del nodo actual apunta al nuevo nodo
            if siguiente_nodo:                                       # Verifica si hay un nodo siguiente al nodo actual
                siguiente_nodo.anterior = nuevo_nodo                 # Si hay un nodo siguiente, el enlace anterior de ese nodo apunta al nuevo nodo
            else:
                self.fin = nuevo_nodo                                # Si no hay un nodo siguiente, el nuevo nodo se convierte en el último nodo de la lista

    def imprimir_adelante(self):
        actual = self.inicio
        while actual:
            print(actual.dato, end=" -> ")                          # Imprime el dato del nodo actual
            actual = actual.siguiente                               # Avanza al siguiente nodo en la lista
        print("None")                                               # Imprime "None" al final de la lista

    def imprimir_atras(self):
        actual = self.fin
        while actual:
            print(actual.dato, end=" -> ")                         # Imprime el dato del nodo actual
            actual = actual.anterior                               # Retrocede al nodo anterior en la lista
        print("None")                                              # Imprime "None" al final de la lista

lista = ListaEnlazadaDoble()
lista.insertar_al_final(1)
lista.insertar_al_final(2)                                         # Crear lista original
lista.insertar_al_final(3)
lista.insertar_al_final(4)
lista.insertar_al_final(5)

lista.insertar_en_posicion(15, 3)                                  # Insertar nodo en posición 3 con dato 15

print("Lista hacia adelante:")
lista.imprimir_adelante()                                          # Imprime hacia adelante

print("\nLista hacia atrás:")
lista.imprimir_atras()                                             # Imprime hacia atras



"""
LA IMPRESIÓN FINAL SERÁ:

Lista hacia adelante:
1 -> 2 -> 15 -> 3 -> 4 -> 5 -> None

Lista hacia atrás:
5 -> 4 -> 3 -> 15 -> 2 -> 1 -> None

"""






