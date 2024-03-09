"""
EJERCICIO 9:   Validar operadores anidados

Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una pila

"""


class Pila:
    def __init__(self):
        self.items = []                                                            # Inicializa una lista vacía para almacenar los elementos de la pila

    def esta_vacia(self):
        return self.items == []                                                    # Verifica si la pila está vacía

    def apilar(self, item):
        self.items.append(item)                                                    # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        if not self.esta_vacia():                                                  # Verifica si la pila no está vacía antes de desapilar
            return self.items.pop()                                                # Elimina y devuelve el elemento en la parte superior de la pila
        else:
            return None                                                            # Si la pila está vacía, devuelve None

def validar_expresion(expresion):
    pila = Pila()                                                                  # Crea una instancia de la clase Pila para almacenar los operadores
    for char in expresion:                                                         # Itera sobre cada caracter de la expresión
        if char in "([{":                                                          # Si el caracter es un paréntesis, corchete o llave de apertura
            pila.apilar(char)                                                      # Apila el caracter en la pila
        elif char in ")]}":                                                        # Si el caracter es un paréntesis, corchete o llave de cierre
            if pila.esta_vacia():                                                  # Verifica si la pila está vacía
                return False                                                       # Si la pila está vacía y hay un cierre sin un correspondiente apertura, la expresión es inválida
            tope = pila.desapilar()                                                # Desapila el último elemento de la pila
            if (tope == "(" and char != ")") or \
               (tope == "[" and char != "]") or \
               (tope == "{" and char != "}"):                                      # Verifica si los operadores coinciden (apertura y cierre)
                return False                                                       # Si los operadores no coinciden, la expresión es inválida
    return pila.esta_vacia()                                                       # Al finalizar, verifica si la pila está vacía (si quedan operadores sin cerrar, la expresión es inválida)

expresion1 = "((2 + 3) * [4 - 1])"                                                 # Expresión con operadores correctamente anidados
expresion2 = "{(5 + 6) * 2]"                                                       # Expresión con operadores incorrectamente anidados

print("Expresión 1:", "Válida" if validar_expresion(expresion1) else "No válida")  # Imprime si la expresión 1 es válida o no
print("Expresión 2:", "Válida" if validar_expresion(expresion2) else "No válida")  # Imprime si la expresión 2 es válida o no



"""
LA IMPRESIÓN FINAL SERÁ:

Expresión 1: Válida
Expresión 2: No válida

"""

