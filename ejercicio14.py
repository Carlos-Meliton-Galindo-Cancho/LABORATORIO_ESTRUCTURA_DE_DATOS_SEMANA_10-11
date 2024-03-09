"""
EJERCICIO 14:    Simular el proceso de deshacer (undo)

Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los deshaceres

"""


class SistemaDeshacer:
    def __init__(self):
        self.acciones = []
        self.deshacer = []

    def hacer(self, accion):
        self.acciones.append(accion)
        # Cuando se realiza una nueva acción, la pila de deshacer se reinicia
        self.deshacer = []

    def deshacer_accion(self):
        if self.acciones:
            accion_deshacer = self.acciones.pop()
            self.deshacer.append(accion_deshacer)
            print("Deshaciendo:", accion_deshacer)
        else:
            print("No hay acciones para deshacer")

    def rehacer_accion(self):
        if self.deshacer:
            accion_rehacer = self.deshacer.pop()
            self.acciones.append(accion_rehacer)
            print("Rehaciendo:", accion_rehacer)
        else:
            print("No hay acciones para rehacer")

# Ejemplo de uso
sistema = SistemaDeshacer()

# Realizar algunas acciones
sistema.hacer("Editar texto")
sistema.hacer("Guardar archivo")
sistema.hacer("Cerrar sesión")

# Deshacer una acción
sistema.deshacer_accion()

# Deshacer otra acción
sistema.deshacer_accion()

# Rehacer una acción
sistema.rehacer_accion()
