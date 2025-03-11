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

estado = Estados();
print(estado.GetNombre());


"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install pyodbc
"""