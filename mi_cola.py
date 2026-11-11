from pasajero import Pasajero


class MiCola:
    """Cola FIFO manual. Las consultas ordenadas trabajan con copias auxiliares,
    nunca cambian el orden de llegada almacenado en datos.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0
        self.reservas = [None] * capacidad
        self.cantidad_reservas = 0

    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def validar_pasajero(self, pasajero):
        if pasajero.numero <= 0:
            return "El número debe ser positivo."
        if pasajero.nombre.strip() == "":
            return "El nombre es obligatorio."
        if pasajero.cedula.strip() == "" or not pasajero.cedula.isdigit():
            return "La cédula debe contener solo números."
        if pasajero.edad < 0 or pasajero.edad > 120:
            return "La edad debe estar entre 0 y 120."
        if pasajero.fecha_vuelo.strip() == "":
            return "La fecha del vuelo es obligatoria."
        if pasajero.destino.strip() == "":
            return "El destino es obligatorio."
        if pasajero.asiento.strip() == "":
            return "El asiento es obligatorio."
        for i in range(self.cantidad):
            actual = self.datos[i]
            if actual.numero == pasajero.numero:
                return "Ya existe ese número de pasajero."
            if actual.cedula == pasajero.cedula:
                return "Esa cédula ya está registrada en la cola."
            if actual.fecha_vuelo == pasajero.fecha_vuelo and actual.asiento == pasajero.asiento:
                return "Ese asiento ya está ocupado para esa fecha."
        return None

    def encolar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  La cola está llena.")
            return False
        error = self.validar_pasajero(pasajero)
        if error is not None:
            print("  Validación: " + error)
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad += 1
        return True

    def listar(self):
        if self.esta_vacia():
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):
            marca = " ← FRENTE" if i == 0 else (" ← FINAL" if i == self.cantidad - 1 else "")
            print(f"  [{i}] {self.datos[i]}{marca}")

    def desencolar(self):
        if self.esta_vacia():
            return None
        pasajero = self.datos[0]
        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
        self.cantidad -= 1
        self.datos[self.cantidad] = None
        return pasajero

    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.datos[0]

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        for i in range(self.cantidad):
            if i != pos and self.datos[i].fecha_vuelo == self.datos[pos].fecha_vuelo and self.datos[i].asiento == nuevo_asiento:
                return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        encontrado = None
        vueltas = self.cantidad
        for _ in range(vueltas):
            pasajero = self.desencolar()
            if pasajero.numero == numero and encontrado is None:
                encontrado = pasajero
            else:
                self.encolar(pasajero)
        return encontrado

    def copiar(self):
        copia = MiCola(self.capacidad)
        for i in range(self.cantidad):
            copia.encolar(self.datos[i])
        return copia

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0

    # Funciones adicionales solicitadas: no modifican la cola FIFO original.
    def _copia_ordenada(self, ascendente=True):
        auxiliar = [None] * self.cantidad
        for i in range(self.cantidad):
            auxiliar[i] = self.datos[i]
        # Ordenamiento por inserción manual sobre el arreglo auxiliar.
        for i in range(1, self.cantidad):
            actual = auxiliar[i]
            j = i - 1
            while j >= 0 and ((auxiliar[j].numero > actual.numero) if ascendente else (auxiliar[j].numero < actual.numero)):
                auxiliar[j + 1] = auxiliar[j]
                j -= 1
            auxiliar[j + 1] = actual
        return auxiliar

    def ordenar_asc(self):
        if self.esta_vacia():
            print("  No hay pasajeros para ordenar.")
            return
        auxiliar = self._copia_ordenada(True)
        print("  Vista ordenada ascendente por número (la cola original no cambia):")
        for i in range(self.cantidad):
            print(f"  [{i}] {auxiliar[i]}")

    def ordenar_desc(self):
        if self.esta_vacia():
            print("  No hay pasajeros para ordenar.")
            return
        auxiliar = self._copia_ordenada(False)
        print("  Vista ordenada descendente por número (la cola original no cambia):")
        for i in range(self.cantidad):
            print(f"  [{i}] {auxiliar[i]}")

    def busqueda_binaria(self, numero):
        if self.esta_vacia():
            return -1
        auxiliar = self._copia_ordenada(True)
        izquierda = 0
        derecha = self.cantidad - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if auxiliar[medio].numero == numero:
                return auxiliar[medio]
            if auxiliar[medio].numero < numero:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return None

    def reservar(self, pasajero):
        """Registra una reserva pendiente sin alterar la fila de pasajeros en espera."""
        if self.cantidad_reservas == self.capacidad:
            return False, "La lista de reservas está llena."
        if pasajero.numero <= 0 or pasajero.nombre.strip() == "" or pasajero.cedula.strip() == "" or not pasajero.cedula.isdigit():
            return False, "Datos de reserva inválidos: revise número, nombre y cédula."
        for i in range(self.cantidad):
            if self.datos[i].numero == pasajero.numero or self.datos[i].cedula == pasajero.cedula:
                return False, "El pasajero ya está registrado en la cola."
        for i in range(self.cantidad_reservas):
            if self.reservas[i].numero == pasajero.numero or self.reservas[i].cedula == pasajero.cedula:
                return False, "Ya existe una reserva con ese número o cédula."
        self.reservas[self.cantidad_reservas] = pasajero
        self.cantidad_reservas += 1
        return True, "Reserva registrada correctamente."

    def listar_reservas(self):
        if self.cantidad_reservas == 0:
            print("  No hay reservas pendientes.")
            return
        print("  RESERVAS:")
        for i in range(self.cantidad_reservas):
            print(f"  [{i}] {self.reservas[i]}")
