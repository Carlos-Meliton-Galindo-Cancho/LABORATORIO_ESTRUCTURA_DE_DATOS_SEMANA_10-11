"""
EJERCICIO 13:    Comprobar palíndromos

Utilizar una pila para comprobar si una palabra o frase es un palíndromo

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

def es_palindromo(palabra):
    # Eliminar espacios en blanco y convertir a minúsculas
    palabra = palabra.replace(" ", "").lower()
    # Crear una pila
    pila = Pila()
    longitud = len(palabra)

    # Apilar la primera mitad de los caracteres en la pila
    for i in range(longitud // 2):
        pila.apilar(palabra[i])

    # Desplazarse a la mitad de la palabra si es impar
    if longitud % 2 != 0:
        i += 1

    # Comparar los caracteres restantes con los desapilados de la pila
    while i < longitud:
        if palabra[i] != pila.desapilar():
            return False
        i += 1

    return True

# Ejemplo de uso
palabra = "reconocer"
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')







