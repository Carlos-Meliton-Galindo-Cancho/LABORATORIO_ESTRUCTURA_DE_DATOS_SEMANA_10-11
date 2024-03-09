"""
EJERCICIO 8:   Evaluar expresión posfija

Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila

"""


class Pila:
    def __init__(self):
        self.items = []                                                                    # Inicializa una lista vacía para almacenar los elementos de la pila

    def esta_vacia(self):
        return self.items == []                                                            # Verifica si la pila está vacía

    def apilar(self, item):
        self.items.append(item)                                                            # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        return self.items.pop()                                                            # Elimina y devuelve el elemento en la parte superior de la pila

def evaluar_expresion_posfija(expresion):
    pila = Pila()                                                                          # Crea una instancia de la clase Pila para almacenar los operandos

    operadores = {'+': lambda x, y: x + y,                                                 # Define diccionario de operadores y funciones correspondientes
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    for caracter in expresion.split():                                                     # Itera sobre los caracteres de la expresión posfija
        if caracter.isdigit():                                                             # Verifica si el caracter es un dígito
            pila.apilar(int(caracter))                                                     # Apila el operando en la pila como un entero
        else:
            segundo_operando = pila.desapilar()                                            # Desapila el segundo operando de la pila
            primer_operando = pila.desapilar()                                             # Desapila el primer operando de la pila
            resultado = operadores[caracter](primer_operando, segundo_operando)            # Evalúa la expresión con el operador correspondiente
            pila.apilar(resultado)                                                         # Apila el resultado de la operación en la pila

    return pila.desapilar()                                                                # Devuelve el resultado final de la evaluación

expresion_posfija = "3 4 + 2 *"                                                            # Expresión posfija a evaluar
resultado = evaluar_expresion_posfija(expresion_posfija)                                   # Evalúa la expresión posfija
print("Resultado de la expresión posfija '{}':".format(expresion_posfija), resultado)      # Imprime el resultado



"""
LA IMPRESIÓN FINAL SERÁ:

Resultado de la expresión posfija '3 4 + 2 *': 14

"""