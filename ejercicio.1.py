"""
EJERCICIO 1:  Duplicar Nodos

Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista duplicada hacia adelante y hacia atrás

"""


class NodoDoble:
    def __init__(self, dato):
        self.dato = dato                                          # Almacena el dato del nodo
        self.siguiente = None                                     # Inicializa el enlace al siguiente nodo como None
        self.anterior = None                                      # Inicializa el enlace al nodo anterior como None

class ListaEnlazadaDoble:
    def __init__(self):
        self.inicio = None                                        # Inicializa el primer nodo de la lista como None
        self.fin = None                                           # Inicializa el último nodo de la lista como None

    def insertar_al_final(self, dato):
        nuevo_nodo = NodoDoble(dato)                              # Crea un nuevo nodo con el dato dado
        if self.inicio is None:                                   # Verifica si la lista está vacía
            self.inicio = self.fin = nuevo_nodo                   # Si la lista está vacía, el nuevo nodo se convierte en el primer y último nodo
        else:
            nuevo_nodo.anterior = self.fin                        # El enlace anterior del nuevo nodo apunta al nodo que actualmente es el último
            self.fin.siguiente = nuevo_nodo                       # El enlace siguiente del nodo que actualmente es el último apunta al nuevo nodo
            self.fin = nuevo_nodo                                 # El nuevo nodo se convierte en el último nodo de la lista

    def duplicar_nodos(self):
        actual = self.inicio                                      # Comienza desde el primer nodo de la lista
        while actual:
            nuevo_nodo = NodoDoble(actual.dato)                   # Crea un nuevo nodo con el mismo dato que el nodo actual
            siguiente_nodo = actual.siguiente                     # Guarda una referencia al nodo siguiente al nodo actual
            nuevo_nodo.siguiente = siguiente_nodo                 # El enlace siguiente del nuevo nodo apunta al nodo siguiente al nodo actual
            nuevo_nodo.anterior = actual                          # El enlace anterior del nuevo nodo apunta al nodo actual
            actual.siguiente = nuevo_nodo                         # El enlace siguiente del nodo actual apunta al nuevo nodo
            if siguiente_nodo:                                    # Verifica si hay un nodo siguiente al nodo actual
                siguiente_nodo.anterior = nuevo_nodo              # Si hay un nodo siguiente, el enlace anterior de ese nodo apunta al nuevo nodo
            actual = siguiente_nodo                               # Avanza al siguiente nodo en la lista

    def imprimir_adelante(self):
        actual = self.inicio                                      # Comienza desde el primer nodo de la lista
        while actual:
            print(actual.dato, end=" -> ")                        # Imprime el dato del nodo actual
            actual = actual.siguiente                             # Avanza al siguiente nodo en la lista
        print("None")                                             # Imprime "None" al final de la lista

    def imprimir_atras(self):
        actual = self.fin                                         # Comienza desde el último nodo de la lista
        while actual:
            print(actual.dato, end=" -> ")                        # Imprime el dato del nodo actual
            actual = actual.anterior                              # Retrocede al nodo anterior en la lista
        print("None")                                             # Imprime "None" al final de la lista

lista_original = ListaEnlazadaDoble()
lista_original.insertar_al_final(1)
lista_original.insertar_al_final(2)                               # Crear lista original
lista_original.insertar_al_final(3)
lista_original.insertar_al_final(4)

lista_original.duplicar_nodos()                                   # Duplicar nodos

print("Lista original hacia adelante:")
lista_original.imprimir_adelante()                                # Imprime la lista original hacia adelante

print("\nLista original hacia atrás:")
lista_original.imprimir_atras()                                   # Imprime la lista original hacia atrás



"""
LA IMPRESIÓN FINAL SERÁ:

Lista original hacia adelante:
1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 4 -> None

Lista original hacia atrás:
4 -> 3 -> 3 -> 2 -> 2 -> 1 -> 1 -> None

"""