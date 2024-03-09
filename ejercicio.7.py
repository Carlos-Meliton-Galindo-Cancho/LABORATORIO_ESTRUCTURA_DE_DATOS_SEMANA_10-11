"""
EJERCICIO 7:   Convertir número decimal a binario

Implementar un programa que convierta un número decimal a su representación en sistema binario utilizando una pila

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

def decimal_a_binario(decimal):
    pila = Pila()

    while decimal > 0:
        residuo = decimal % 2
        pila.apilar(residuo)
        decimal //= 2

    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())

    return binario

# Ejemplo de uso
numero_decimal = 19
binario = decimal_a_binario(numero_decimal)
print(f"El número decimal {numero_decimal} en binario es: {binario}")














