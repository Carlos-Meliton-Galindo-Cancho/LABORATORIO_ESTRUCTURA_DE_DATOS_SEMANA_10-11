"""
EJERCICIO 14:    Simular el proceso de deshacer (undo)

Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los deshaceres

"""


class SistemaDeshacer:
    def __init__(self):
        self.acciones = []                                            # Lista para almacenar las acciones realizadas
        self.deshacer = []                                            # Lista para almacenar las acciones deshechas

    def hacer(self, accion):
        self.acciones.append(accion)                                  # Agrega la acción a la lista de acciones realizadas
        self.deshacer = []                                            # Cuando se realiza una nueva acción, la lista de acciones deshechas se reinicia

    def deshacer_accion(self):
        if self.acciones:                                             # Verifica si hay acciones para deshacer
            accion_deshacer = self.acciones.pop()                     # Extrae la última acción realizada
            self.deshacer.append(accion_deshacer)                     # Agrega la acción a la lista de acciones deshechas
            print("Deshaciendo:", accion_deshacer)                    # Imprime la acción que se está deshaciendo
        else:
            print("No hay acciones para deshacer")                    # Imprime un mensaje si no hay acciones para deshacer

    def rehacer_accion(self):
        if self.deshacer:                                             # Verifica si hay acciones para rehacer
            accion_rehacer = self.deshacer.pop()                      # Extrae la última acción deshecha
            self.acciones.append(accion_rehacer)                      # Agrega la acción de vuelta a la lista de acciones realizadas
            print("Rehaciendo:", accion_rehacer)                      # Imprime la acción que se está rehaciendo
        else:
            print("No hay acciones para rehacer")                     # Imprime un mensaje si no hay acciones para rehacer

sistema = SistemaDeshacer()                                           # Instancia un objeto de la clase SistemaDeshacer

sistema.hacer("Editar texto")
sistema.hacer("Guardar archivo")                                      # Realizar algunas acciones
sistema.hacer("Cerrar sesión")

sistema.deshacer_accion()                                             # Deshacer una acción

sistema.deshacer_accion()                                             # Deshacer otra acción

sistema.rehacer_accion()                                              # Rehacer una acción



"""
LA IMPRESIÓN FINAL SERÁ:

Deshaciendo: Cerrar sesión
Deshaciendo: Guardar archivo
Rehaciendo: Guardar archivo

"""