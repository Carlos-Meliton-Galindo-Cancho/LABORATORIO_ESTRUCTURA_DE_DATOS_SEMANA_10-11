"""
EJERCICIO 4:  Eliminar Nodos Duplicados

Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás

"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato                                          # Almacena el dato del nodo
        self.siguiente = None                                     # Inicializa el enlace al siguiente nodo como None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None                                        # Inicializa la cabeza de la lista como None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)                                   # Crea un nuevo nodo con el dato dado
        if not self.cabeza:                                       # Verifica si la lista está vacía
            self.cabeza = nuevo_nodo                              # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo                         # Si la lista no está vacía, se agrega el nuevo nodo al final

    def eliminar_duplicados(self):
        datos_vistos = set()                                      # Crea un conjunto para almacenar los datos vistos
        actual = self.cabeza                                      # Comienza desde la cabeza de la lista
        previo = None                                             # Inicializa el nodo previo como None
        while actual:                                             # Itera sobre la lista
            if actual.dato in datos_vistos:                       # Verifica si el dato actual ya ha sido visto
                previo.siguiente = actual.siguiente               # Elimina el nodo actual enlazando el nodo previo con el siguiente al actual
                del actual                                        # Elimina el nodo actual
                actual = previo.siguiente                         # Avanza al siguiente nodo después del nodo previo
            else:
                datos_vistos.add(actual.dato)                     # Agrega el dato actual al conjunto de datos vistos
                previo = actual                                   # El nodo actual se convierte en el nodo previo
                actual = actual.siguiente                         # Avanza al siguiente nodo en la lista

    def imprimir_adelante(self):
        actual = self.cabeza                                      # Comienza desde la cabeza de la lista
        while actual:                                             # Itera sobre la lista
            print(actual.dato, end=" -> ")                        # Imprime el dato del nodo actual
            actual = actual.siguiente                             # Avanza al siguiente nodo en la lista
        print("None")                                             # Imprime "None" al final de la lista

    def imprimir_atras(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza                                    # Si no se proporciona un nodo, comienza desde la cabeza de la lista
        if nodo:                                                  # Verifica si el nodo actual es válido
            self.imprimir_atras(nodo.siguiente)                   # Realiza una llamada recursiva para avanzar hacia el final de la lista
            print(nodo.dato, end=" -> ")                          # Imprime el dato del nodo actual

lista = ListaEnlazada()                                           # Crear la lista enlazada con datos duplicados
datos = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
for dato in datos:
    lista.insertar(dato)

lista.eliminar_duplicados()                                       # Eliminar nodos duplicados

print("Lista sin nodos duplicados hacia adelante:")               # Imprimir la lista hacia adelante y hacia atrás
lista.imprimir_adelante()                                         # Imprime la lista sin nodos duplicados hacia adelante
print("Lista sin nodos duplicados hacia atrás:")
lista.imprimir_atras()                                            # Imprime la lista sin nodos duplicados hacia atrás



