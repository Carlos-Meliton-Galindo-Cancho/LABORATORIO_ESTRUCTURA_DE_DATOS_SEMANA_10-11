"""
EJERCICIO 9:   Validar operadores anidados

Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una pila

"""


class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def validar_expresion(expresion):
    pila = Pila()
    for char in expresion:
        if char in "([{":
            pila.apilar(char)
        elif char in ")]}":
            if pila.esta_vacia():
                return False
            tope = pila.desapilar()
            if (tope == "(" and char != ")") or \
               (tope == "[" and char != "]") or \
               (tope == "{" and char != "}"):
                return False
    return pila.esta_vacia()

# Ejemplo de uso
expresion1 = "((2 + 3) * [4 - 1])"
expresion2 = "{(5 + 6) * 2]"

print("Expresión 1:", "Válida" if validar_expresion(expresion1) else "No válida")
print("Expresión 2:", "Válida" if validar_expresion(expresion2) else "No válida")















