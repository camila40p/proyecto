from datetime import datetime

class Seguimiento:
    def __init__(self, id, pedido_id, estado_id, ubicacion, comentario, fecha_hora):
        self.setId(id)
        self.setPedidoId(pedido_id)
        self.setCiudadId(estado_id)
        self.setFechaHora(ubicacion)
        self.setEstado(comentario)
        self.setEstado(fecha_hora)

    def getId(self):
        return self.__id

    def setId(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("Id no válido")

    def getPedidoId(self):
        return self.__pedido_id

    def setPedidoId(self, pedido_id):
        if isinstance(pedido_id, int):
            self.pedido_id = pedido_id
        else:
            raise ValueError("pedido_id no válido")

    def getEstadoId(self):
        return self.__estado_id

    def setEstadoId(self, estado_id):
        if isinstance(estado_id, int):
            self.__estado_id = estado_id
        else:
            raise ValueError("estado_id no válido")

    def getUbicacion(self):
        return self.__ubicacion

    def setubicacion(self, ubicacion):
        if isinstance(ubicacion):
            self.__ubicacion = ubicacion
        else:
            raise ValueError("Ubicacion no válida")

    def getComentario(self):
        return self.__comentario

    def setComentario(self, comentario):
        if isinstance(comentario):
            self.__Comentario = comentario
        else:
            raise ValueError("comentario no válido")
        
    def getFechaHora(self):
        return self.__fecha_hora

    def setFechaHora(self, fecha_hora):
        if isinstance(fecha_hora, datetime):
            self.__fecha_hora = fecha_hora
        else:
            raise ValueError("fecha_hora no válida")