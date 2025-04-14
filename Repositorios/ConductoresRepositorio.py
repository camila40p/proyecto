#Improtar clases de otras carpetas del proyecto
from Nucleo import Conexion;

#Cada entidad es una clase
class ConductoresRepositorio:

    #Insertar conductor     
    def Guardar(self, conductor):
        
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()

        consulta = f"""INSERT INTO Conductores (id,nombre,cedula,telefono) VALUES ({conductor.getId()},'{conductor.getNombre()}','{conductor.getCedula()}','{conductor.getTelefono()}')""";
        
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()

        return True