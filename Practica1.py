
class Vehiculo:
    """
    Clase usada para crear objetos de tipo Vehiculo
    """
    def __init__(self, color, modelo, placa, valor, cilindraje, anio, tipo_puertas,
                 combustible, kilometraje, caja_cambios, seguro, gama, chasis,
                 pais_origen, marca, llanta_emergencia, numero_puertas):
        self._color = color
        self._modelo = modelo
        self._placa = placa
        self._valor = valor
        self._cilindraje = cilindraje
        self._anio = anio
        self._tipo_puertas = tipo_puertas
        self._combustible = combustible
        self._kilometraje = kilometraje
        self._caja_cambios = caja_cambios
        self._seguro = seguro
        self._gama = gama
        self._chasis = chasis
        self._pais_origen = pais_origen
        self._marca = marca
        self._llanta_emergencia = llanta_emergencia
        self._numero_puertas = numero_puertas

    def __str__(self):
        return (f'Vehiculo [Marca: {self._marca}, Modelo: {self._modelo}, Color: {self._color}, Placa: {self._placa}, '
                f'Valor: {self._valor}, Cilindraje: {self._cilindraje}, Año: {self._anio}, Tipo de Puertas: {self._tipo_puertas}, '
                f'Combustible: {self._combustible}, Kilometraje: {self._kilometraje}, Caja de Cambios: {self._caja_cambios}, '
                f'Seguro: {self._seguro}, Gama: {self._gama}, Chasis: {self._chasis}, País de Origen: {self._pais_origen}, '
                f'Llanta de Emergencia: {self._llanta_emergencia}, Número de Puertas: {self._numero_puertas}]')

if __name__ == '__main__':
     objVehiculo1 = Vehiculo(
        color='Rojo',
        modelo='C-X5',
        placa='GSB7589',
        valor=46000,
        cilindraje=5000 ,
        anio=2020,
        tipo_puertas='SUV',
        combustible='Gasolina',
        kilometraje=10000,
        caja_cambios='Automática',
        seguro='Sí',
        gama='Alta',
        chasis='XYZ1234567890',
        pais_origen='Vietnam',
        marca='Mazda',
        llanta_emergencia='Sí',
        numero_puertas=5
     )
     print(objVehiculo1) 