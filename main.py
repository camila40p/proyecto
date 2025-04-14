#Improtar clases de otras carpetas del proyecto
from Entidades import Conductores;
from Repositorios import ConductoresRepositorio;

#Definicion metodo Main
def main():
   
   #Inicializacion de datos
   id=6
   nombre="Jorge luis"
   cedula="1002"
   telefono="300378973"

   #Creo Objeto conductor
   conductor = Conductores.Conductores(id,nombre,cedula,telefono)
   #Creo objeto de repositorio conductores 
   repositorio = ConductoresRepositorio.ConductoresRepositorio();
   #Utilizo metodo guardar que me recibe el objeto conductor
   repositorio.Guardar(conductor);
   
   print("Pruebaaa")


#Llamado metodo Main
if __name__ == "__main__":
    main()