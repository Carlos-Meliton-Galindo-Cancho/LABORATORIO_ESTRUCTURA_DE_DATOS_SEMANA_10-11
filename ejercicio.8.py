"""
EJERCICIO 8:   Evaluar expresión posfija

Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila

"""


class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

def evaluar_expresion_posfija(expresion):
    pila = Pila()

    operadores = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    for caracter in expresion.split():
        if caracter.isdigit():
            pila.apilar(int(caracter))
        else:
            segundo_operando = pila.desapilar()
            primer_operando = pila.desapilar()
            resultado = operadores[caracter](primer_operando, segundo_operando)
            pila.apilar(resultado)

    return pila.desapilar()

# Ejemplo de uso
expresion_posfija = "3 4 + 2 *"
resultado = evaluar_expresion_posfija(expresion_posfija)
print("Resultado de la expresión posfija '{}':".format(expresion_posfija), resultado)
