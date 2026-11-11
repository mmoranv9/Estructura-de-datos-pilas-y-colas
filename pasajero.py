class Pasajero:
    """Representa a un pasajero de la aerolínea."""

    def __init__(self, numero, nombre, cedula, edad, fecha_vuelo, destino, asiento):
        self.numero = numero
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.fecha_vuelo = fecha_vuelo
        self.destino = destino
        self.asiento = asiento

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def __str__(self):
        return (f"#{self.numero} | {self.nombre:<10} | {self.cedula} | "
                f"{self.edad:>2} años | {self.fecha_vuelo} | "
                f"{self.destino:<10} | asiento {self.asiento}")
