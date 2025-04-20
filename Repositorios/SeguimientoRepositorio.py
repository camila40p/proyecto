class SeguimientoRepositorio:
    def Guardar(self, seguimiento):
        print("Guardando seguimiento:", seguimiento.getId())

    def Actualizar(self, seguimiento):
        print("Actualizando seguimiento:", seguimiento.getId())

    def Eliminar(self, seguimiento):
        print("Eliminando seguimiento:", seguimiento.getId())

    def Consultar(self, seguimiento):
        print("Consultando seguimiento:", seguimiento.getId())
