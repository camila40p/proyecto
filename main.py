#Improtar clases de otras carpetas del proyecto
from Entidades import Conductores
from Entidades import Vehiculos
from Repositorios import ConductoresRepositorio
from Repositorios import VehiculosRepositorio

#Definicion metodo Main
def main():
   
   #--CONDUCTOR

   #Inicializacion de datos
   id=1
   nombre="Jorge luis parra"
   cedula="1003"
   telefono="301378973"

   #Insertar
   #Creo Objeto conductor
   #conductor = Conductores.Conductores(id,nombre,cedula,telefono)
   #Creo objeto de repositorio conductores 
   #repositorio = ConductoresRepositorio.ConductoresRepositorio()
   #Utilizo metodo guardar que me recibe el objeto conductor
   #repositorio.Guardar(conductor)
   
   #Actualizar
   #Creo Objeto conductor
   #conductor = Conductores.Conductores(id,nombre,cedula,telefono)
   #Creo objeto de repositorio conductores 
   #repositorio = ConductoresRepositorio.ConductoresRepositorio()
   #Utilizo metodo guardar que me recibe el objeto conductor
   #repositorio.Actualizar(conductor)

   #Eliminar
   #Creo Objeto conductor
   #conductor = Conductores.Conductores(id,nombre,cedula,telefono)
   #Creo objeto de repositorio conductores 
   #repositorio = ConductoresRepositorio.ConductoresRepositorio()
   #Utilizo metodo guardar que me recibe el objeto conductor
   #repositorio.Eliminar(conductor)

   #Consultar
   #Creo Objeto conductor
   #conductor = Conductores.Conductores(id,nombre,cedula,telefono)
   #Creo objeto de repositorio conductores 
   #repositorio = ConductoresRepositorio.ConductoresRepositorio()
   #Utilizo metodo guardar que me recibe el objeto conductor
   #repositorio.Consultar(conductor)

   #--VEHICULO

    #Inicializacion de datos
   id=2
   placa="GH1245"
   tipo="Moto BMW"
   capacidad=160

   #Insertar
   #Creo Objeto vehiculo
   #vehiculo = Vehiculos.Vehiculos(id,placa,tipo,capacidad)
   #Creo objeto de repositorio conductores 
   #repositorio = VehiculosRepositorio.VehiculosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto conductor
   #repositorio.Guardar(vehiculo)


   #Actualizar
   #Creo Objeto vehiculo
   #vehiculo = Vehiculos.Vehiculos(id,placa,tipo,capacidad)
   #Creo objeto de repositorio conductores 
   #repositorio = VehiculosRepositorio.VehiculosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto conductor
   #repositorio.Actualizar(vehiculo)


   #Eliminar
   #Creo Objeto vehiculo
   #vehiculo = Vehiculos.Vehiculos(id,placa,tipo,capacidad)
   #Creo objeto de repositorio conductores 
   #repositorio = VehiculosRepositorio.VehiculosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto conductor
   #repositorio.Eliminar(vehiculo)

   #Consultar
   #Creo Objeto vehiculo
   #vehiculo = Vehiculos.Vehiculos(id,placa,tipo,capacidad)
   #Creo objeto de repositorio conductores 
   #repositorio = VehiculosRepositorio.VehiculosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto conductor
   #repositorio.Consultar(vehiculo)


#Llamado metodo Main
if __name__ == "__main__":
    main()