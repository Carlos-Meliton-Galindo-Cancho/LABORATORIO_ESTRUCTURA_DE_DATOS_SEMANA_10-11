"""
EJERCICIO 12:  Implementar una calculadora sencilla

Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar expresiones.

"""


class Calculadora:
    def __init__(self):
        self.pila = []

    def _operar(self, operador):
        if len(self.pila) < 2:
            raise ValueError("No hay suficientes operandos para operar")
        operando2 = self.pila.pop()
        operando1 = self.pila.pop()
        if operador == '+':
            self.pila.append(operando1 + operando2)
        elif operador == '-':
            self.pila.append(operando1 - operando2)
        elif operador == '*':
            self.pila.append(operando1 * operando2)
        elif operador == '/':
            if operando2 == 0:
                raise ValueError("División por cero")
            self.pila.append(operando1 / operando2)

    def calcular(self, expresion):
        tokens = expresion.split()
        for token in tokens:
            if token.isdigit():
                self.pila.append(int(token))
            elif token in {'+', '-', '*', '/'}:
                self._operar(token)
            else:
                raise ValueError("Token no reconocido: " + token)
        if len(self.pila) != 1:
            raise ValueError("La expresión no está bien formada")
        return self.pila.pop()

calculadora = Calculadora()
expresion = "3 + 4 * 2 / 1"
resultado = calculadora.calcular(expresion)
print("Resultado de la expresión:", resultado)  # Salida: 11.0






