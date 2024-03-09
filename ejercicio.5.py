"""
EJERCICIO 5:  Invertir la Lista

Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el primero y viceversa e imprime la lista hacia adelante y hacia atrás

"""


class NodoDoble:
    def __init__(self, dato):
        self.dato = dato                                           # Almacena el dato del nodo
        self.siguiente = None                                      # Inicializa el enlace al siguiente nodo como None
        self.anterior = None                                       # Inicializa el enlace al nodo anterior como None

class ListaEnlazadaDoble:
    def __init__(self):
        self.inicio = None                                         # Inicializa el primer nodo de la lista como None
        self.fin = None                                            # Inicializa el último nodo de la lista como None

    def insertar_al_final(self, dato):
        nuevo_nodo = NodoDoble(dato)                               # Crea un nuevo nodo con el dato dado
        if self.inicio is None:                                    # Verifica si la lista está vacía
            self.inicio = nuevo_nodo                               # Si la lista está vacía, el nuevo nodo se convierte en el primer y último nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin                         # El enlace anterior del nuevo nodo apunta al nodo que actualmente es el último
            self.fin.siguiente = nuevo_nodo                        # El enlace siguiente del nodo que actualmente es el último apunta al nuevo nodo
            self.fin = nuevo_nodo                                  # El nuevo nodo se convierte en el último nodo de la lista

    def invertir_lista(self):
        actual = self.inicio                                       # Comienza desde el primer nodo de la lista
        while actual:
            siguiente_temp = actual.siguiente                      # Guarda una referencia al siguiente nodo
            actual.siguiente = actual.anterior                     # Invierte el enlace siguiente del nodo actual al nodo anterior
            actual.anterior = siguiente_temp                       # Invierte el enlace anterior del nodo actual al siguiente nodo
            actual = siguiente_temp                                # Avanza al siguiente nodo en la lista
       
        self.inicio, self.fin = self.fin, self.inicio              # Cambia los punteros de inicio y fin para reflejar la nueva orientación de la lista

    def imprimir_adelante(self):
        actual = self.inicio                                       # Comienza desde el primer nodo de la lista
        while actual:
            print(actual.dato, end=" -> ")                         # Imprime el dato del nodo actual
            actual = actual.siguiente                              # Avanza al siguiente nodo en la lista
        print("None")                                              # Imprime "None" al final de la lista

    def imprimir_atras(self):
        actual = self.fin                                          # Comienza desde el último nodo de la lista
        while actual:
            print(actual.dato, end=" -> ")                         # Imprime el dato del nodo actual
            actual = actual.anterior                               # Retrocede al nodo anterior en la lista
        print("None")                                              # Imprime "None" al final de la lista

lista = ListaEnlazadaDoble()                                       # Crear lista original
for i in range(1, 7):
    lista.insertar_al_final(i)

lista.invertir_lista()                                             # Invertir la lista

print("Lista invertida hacia adelante:")
lista.imprimir_adelante()                                          # Imprime la lista invertida hacia adelante

print("\nLista invertida hacia atrás:")
lista.imprimir_atras()                                             # Imprime la lista invertida hacia atrás



"""
LA IMPRESIÓN FINAL SERÁ:

Lista invertida hacia adelante:
6 -> 5 -> 4 -> 3 -> 2 -> 1 -> None

Lista invertida hacia atrás:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

"""