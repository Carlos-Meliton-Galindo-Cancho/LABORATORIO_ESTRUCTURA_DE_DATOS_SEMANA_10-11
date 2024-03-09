"""
EJERCICIO 12:  Implementar una calculadora sencilla

Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar expresiones.

"""


class Calculadora:
    def __init__(self):
        self.pila = []                                                      # Inicializa una lista vacía para almacenar los operandos y resultados de las operaciones

    def _operar(self, operador):                                            # Método privado para realizar la operación correspondiente según el operador y los operandos en la pila
        if len(self.pila) < 2:                                              # Verifica si hay suficientes operandos para realizar la operación
            raise ValueError("No hay suficientes operandos para operar")
        operando2 = self.pila.pop()                                         # Extrae el segundo operando de la pila
        operando1 = self.pila.pop()                                         # Extrae el primer operando de la pila
        
        if operador == '+':                                                 # Realiza la operación correspondiente según el operador y apila el resultado nuevamente
            self.pila.append(operando1 + operando2)
        elif operador == '-':
            self.pila.append(operando1 - operando2)
        elif operador == '*':
            self.pila.append(operando1 * operando2)
        elif operador == '/':
            if operando2 == 0:                                              # Verifica si se está intentando dividir por cero
                raise ValueError("División por cero")
            self.pila.append(operando1 / operando2)

    def calcular(self, expresion):
        tokens = expresion.split()                                          # Divide la expresión en tokens separados por espacios
        for token in tokens:
            if token.isdigit():                                             # Verifica si el token es un número entero
                self.pila.append(int(token))                                # Convierte el token a entero y lo apila en la pila
            elif token in {'+', '-', '*', '/'}:                             # Verifica si el token es un operador
                self._operar(token)                                         # Llama al método privado para realizar la operación correspondiente
            else:
                raise ValueError("Token no reconocido: " + token)           # Levanta una excepción si el token no es reconocido
        if len(self.pila) != 1:                                             # Verifica si la pila tiene exactamente un elemento al final de la evaluación
            raise ValueError("La expresión no está bien formada")           # Levanta una excepción si la expresión no está bien formada
        return self.pila.pop()                                              # Devuelve el resultado final de la evaluación de la expresión

calculadora = Calculadora()                                                 # Crea una instancia de la calculadora
expresion = "3 + 4 * 2 / 1"                                                 # Define la expresión a evaluar
resultado = calculadora.calcular(expresion)                                 # Llama al método calcular para obtener el resultado
print("Resultado de la expresión:", resultado)                              # Imprime el resultado obtenido



"""
LA IMPRESIÓN FINAL SERÁ:

ValueError: No hay suficientes operandos para operar

"""