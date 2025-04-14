#Improtar clases de otras carpetas del proyecto
from Entidades import Conductores
from Entidades import Vehiculos
from Entidades import Tipo_Envio
from Entidades import Usuarios
from Repositorios import ConductoresRepositorio
from Repositorios import VehiculosRepositorio
from Repositorios import TipoEnvioRepositorio
from Repositorios import UsuariosRepositorio

from datetime import datetime

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
   #Creo objeto de repositorio vehiculo
   #repositorio = VehiculosRepositorio.VehiculosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto vehiculo
   #repositorio.Guardar(vehiculo)


   #Actualizar
   #Creo Objeto vehiculo
   #vehiculo = Vehiculos.Vehiculos(id,placa,tipo,capacidad)
   #Creo objeto de repositorio vehiculo
   #repositorio = VehiculosRepositorio.VehiculosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto vehiculo
   #repositorio.Actualizar(vehiculo)


   #Eliminar
   #Creo Objeto vehiculo
   #vehiculo = Vehiculos.Vehiculos(id,placa,tipo,capacidad)
   #Creo objeto de repositorio vehiculo
   #repositorio = VehiculosRepositorio.VehiculosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto vehiculo
   #repositorio.Eliminar(vehiculo)

   #Consultar
   #Creo Objeto vehiculo
   #vehiculo = Vehiculos.Vehiculos(id,placa,tipo,capacidad)
   #Creo objeto de repositorio vehiculo
   #repositorio = VehiculosRepositorio.VehiculosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto vehiculo
   #repositorio.Consultar(vehiculo)


   #--TIPO ENVIO

    #Inicializacion de datos
   id=2
   nombre="Delicado2"

   #Insertar
   #Creo Objeto envio
   #tipoenvio = Tipo_Envio.Tipo_Envio(id,nombre)
   #Creo objeto de repositorio tipo envio 
   #repositorio = TipoEnvioRepositorio.TipoEnvioRepositorio()
   #Utilizo metodo guardar que me recibe el objeto envio
   #repositorio.Guardar(tipoenvio)


   #Actualizar
   #Creo Objeto envio
   #tipoenvio = Tipo_Envio.Tipo_Envio(id,nombre)
   #Creo objeto de repositorio envio
   #repositorio = TipoEnvioRepositorio.TipoEnvioRepositorio()
   #Utilizo metodo guardar que me recibe el objeto envio
   #repositorio.Actualizar(tipoenvio)


   #Eliminar
   #Creo Objeto envio
   #tipoenvio = Tipo_Envio.Tipo_Envio(id,nombre)
   #Creo objeto de repositorio envio
   #repositorio = TipoEnvioRepositorio.TipoEnvioRepositorio()
   #Utilizo metodo guardar que me recibe el objeto envio
   #repositorio.Eliminar(tipoenvio)

   #Consultar
   #Creo Objeto envio
   #tipoenvio = Tipo_Envio.Tipo_Envio(id,nombre)
   #Creo objeto de repositorio envio
   #repositorio = TipoEnvioRepositorio.TipoEnvioRepositorio()
   #Utilizo metodo guardar que me recibe el objeto envio
   #repositorio.Consultar(tipoenvio)


   #--USUARIOS

    #Inicializacion de datos
   id=2
   nombre="Jorge luis parra garcia"
   email="jorge123@gmail.com"
   telefono="3014784269"
   direccion="Calle 39 "
   rol="Administrador"
   fechaRegistro=datetime(2025, 4, 10, 16, 30, 0) 
   
   #Insertar
   #Creo Objeto usuario
   #usuario = Usuarios.Usuarios(id,nombre,email,telefono,direccion,rol,fechaRegistro)
   #Creo objeto de repositorio usuario
   #repositorio = UsuariosRepositorio.UsuariosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto usuario
   #repositorio.Guardar(usuario)


   #Actualizar
   #Creo Objeto usuario
   #usuario = Usuarios.Usuarios(id,nombre,email,telefono,direccion,rol,fechaRegistro)
   #Creo objeto de repositorio usuario
   #repositorio = UsuariosRepositorio.UsuariosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto usuario
   #repositorio.Actualizar(usuario)

   #Eliminar
   #Creo Objeto usuario
   #usuario = Usuarios.Usuarios(id,nombre,email,telefono,direccion,rol,fechaRegistro)
   #Creo objeto de repositorio usuario
   #repositorio = UsuariosRepositorio.UsuariosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto usuario
   #repositorio.Eliminar(usuario)

   #Consultar
   #Creo Objeto usuario
   usuario = Usuarios.Usuarios(id,nombre,email,telefono,direccion,rol,fechaRegistro)
   #Creo objeto de repositorio usuario
   repositorio = UsuariosRepositorio.UsuariosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto usuario
   repositorio.Consultar(usuario)





#Llamado metodo Main
if __name__ == "__main__":
    main()