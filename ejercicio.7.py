"""
EJERCICIO 7:   Convertir número decimal a binario

Implementar un programa que convierta un número decimal a su representación en sistema binario utilizando una pila

"""


class Pila:
    def __init__(self):
        self.items = []                                                       # Inicializa una lista vacía para almacenar los elementos de la pila

    def esta_vacia(self):
        return self.items == []                                               # Verifica si la pila está vacía

    def apilar(self, item):
        self.items.append(item)                                               # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        if not self.esta_vacia():                                             # Verifica si la pila no está vacía
            return self.items.pop()                                           # Elimina y devuelve el elemento en la parte superior de la pila

def decimal_a_binario(decimal):
    pila = Pila()                                                             # Crea una instancia de la clase Pila para almacenar los residuos
    while decimal > 0:                                                        # Mientras el número decimal sea mayor que 0
        residuo = decimal % 2                                                 # Calcula el residuo de la división por 2
        pila.apilar(residuo)                                                  # Apila el residuo obtenido
        decimal //= 2                                                         # Divide el número decimal por 2 para continuar con la siguiente iteración

    binario = ""                                                              # Inicializa una cadena vacía para almacenar la representación binaria del número
    while not pila.esta_vacia():                                              # Mientras la pila no esté vacía
        binario += str(pila.desapilar())                                      # Desapila los residuos y los agrega a la cadena binaria

    return binario                                                            # Devuelve la representación binaria del número decimal

numero_decimal = 19                                                           # Número decimal a convertir
binario = decimal_a_binario(numero_decimal)                                   # Convierte el número decimal a binario
print(f"El número decimal {numero_decimal} en binario es: {binario}")         # Imprime el resultado



"""
LA IMPRESIÓN FINAL SERÁ:

El número decimal 19 en binario es: 10011

"""

