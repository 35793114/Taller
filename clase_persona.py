class Empleado:
	'''
	crear objetos de la clase Empleado
	'''
	def __init__(self, nombre, sueldo, eliminado):
		'''
		Constructor de la clase empleado
		:param nombre: nombre del empleado
		:param sueldo: sueldo del empleado
		:param eliminado: True si esta eliminado, False si no esta eliminado
		'''
		self._nombre = nombre
		self._sueldo = sueldo
		self._eliminado = eliminado
	@property
	def nombre(self):
		return self._nombre
	@nombre.setter
	def nombre(self, nombre):
		self._nombre = nombre