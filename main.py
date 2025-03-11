import datetime;
import decimal;
import pyodbc;

"""
	varInteger: int = 253; # int(253);
	varLong: int = 2350006657; # int(2350006657);
	varFloat: float = 10.5; float(10.2);
	varDecimal: decimal = 15.6;
	varString: str = "Test"; # str("Valor 2");
	varDate: datetime = datetime.datetime.now();
	varBool: bool = True; # bool(True);
"""

# DTO, ENTIDAD...
class Estados:
	id: int = 0;

	def GetId(self) -> int:
		return self.id;
	def SetId(self, value: int) -> None:
		self.id = value;

	nombre: str = None;

	def GetNombre(self) -> str:
		return self.nombre;
	def SetNombre(self, value: str) -> None:
		self.nombre = value;

class Personas:
	id: int = 0;

	def GetId(self) -> int:
		return self.id;
	def SetId(self, value: int) -> None:
		self.id = value;

	cedula: str = None;

	def GetCedula(self) -> str:
		return self.cedula;
	def SetCedula(self, value: str) -> None:
		self.cedula = value;

	nombre: str = None;

	def GetNombre(self) -> str:
		return self.nombre;
	def SetNombre(self, value: str) -> None:
		self.nombre = value;

	estado: int = None;

	def GetEstado(self) -> int:
		return self.estado;
	def SetEstado(self, value: int) -> None:
		self.estado = value;

	fecha: datetime = None;

	def GetFecha(self) -> datetime:
		return self.fecha;
	def SetFecha(self, value: datetime) -> None:
		self.fecha = value;

	activo: bool = None;

	def GetActivo(self) -> bool:
		return self.activo;
	def SetActivo(self, value: bool) -> None:
		self.activo = value;

	_estado: Estados = None;

	def Get_Estado(self) -> Estados:
		return self._estado;
	def Set_Estado(self, value: Estados) -> None:
		self._estado = value;

# REPOSITORIO
class Repositorio:
	strConnection: str = """
		Driver={MySQL ODBC 9.0 Unicode Driver};
		Server=localhost;
		Database=db_personas;
		PORT=3306;
		user=user_ptyhon;
		password=Clas3s1Nt2024_!""";

	def ConexionBasica(self) -> None:
		conexion = pyodbc.connect(self.strConnection);

		consulta: str = """SELECT * FROM estados""";
		cursor = conexion.cursor();
		cursor.execute(consulta);

		for elemento in cursor:
			print(elemento);

		cursor.close();
		conexion.close();

	def ConexionBasica2(self) -> None:
		conexion = pyodbc.connect(self.strConnection);

		consulta: str = """SELECT * FROM estados""";
		cursor = conexion.cursor();
		cursor.execute(consulta);

		lista: list = [];
		for elemento in cursor:
			entidad: Estados = Estados();
			entidad.SetId(elemento[0]);
			entidad.SetNombre(elemento[1]);
			lista.append(entidad);

		cursor.close();
		conexion.close();

		for estado in lista:
			print(str(estado.GetId()) + ", " + estado.GetNombre());

	def ConexionBasica3(self) -> None:
		conexion = pyodbc.connect(self.strConnection);

		consulta: str = """SELECT p.id,
				p.cedula,
				p.nombre,
				p.estado,
				p.fecha,
				p.activo,
				e.id,
				e.nombre
			FROM `personas` p INNER JOIN `estados` e ON p.estado = e.id;""";
		cursor = conexion.cursor();
		cursor.execute(consulta);

		for elemento in cursor:
			print(elemento);

		cursor.close();
		conexion.close();

	def ConexionBasica4(self) -> None:
		conexion = pyodbc.connect(self.strConnection);

		consulta: str = """INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Test');""";
		cursor = conexion.cursor();
		cursor.execute(consulta);
		cursor.commit();

		cursor.close();
		conexion.close();

estado = Estados();
print(estado.GetNombre());

repositorio = Repositorio();
# repositorio.ConexionBasica();
# repositorio.ConexionBasica2();
# repositorio.ConexionBasica3();
repositorio.ConexionBasica4();

"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install pyodbc
"""