"""
EJERCICIO 2:  Contar Nodos Pares e Impares

Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato impar e imprime la lista hacia adelante y hacia atrás

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

    def contar_pares_impares(self):
        actual = self.cabeza
        pares = 0
        impares = 0
        while actual:
            if actual.dato % 2 == 0:                              # Verifica si el dato del nodo es par
                pares += 1
            else:
                impares += 1                                      # Si no es par, se considera impar
            actual = actual.siguiente
        return pares, impares                                     # Retorna la cantidad de nodos pares e impares

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")                        # Imprime el dato del nodo actual
            actual = actual.siguiente                             # Avanza al siguiente nodo en la lista
        print("None")                                             # Imprime "None" al final de la lista

    def imprimir_atras(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo:
            self.imprimir_atras(nodo.siguiente)                  # Realiza una llamada recursiva para avanzar hacia el último nodo
            print(nodo.dato, end=" -> ")                         # Imprime el dato del nodo actual

lista = ListaEnlazada()                                          # Crear la lista enlazada
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9]                              # Datos para insertar en la lista
for dato in datos:
    lista.insertar(dato)

pares, impares = lista.contar_pares_impares()                    # Contar nodos pares e impares
print("Cantidad de nodos pares:", pares)
print("Cantidad de nodos impares:", impares)

print("Lista hacia adelante:")                                   # Imprimir la lista hacia adelante y hacia atrás
lista.imprimir_adelante()                                        # Imprime la lista hacia adelante
print("Lista hacia atrás:")
lista.imprimir_atras()                                           # Imprime la lista hacia atrás


