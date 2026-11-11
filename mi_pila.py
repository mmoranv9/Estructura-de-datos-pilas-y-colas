from pasajero import Pasajero


class MiPila:
    """Pila LIFO implementada manualmente con un arreglo fijo."""

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return i
        return -1

    def apilar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  La pila está llena.")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  Ya existe un pasajero con ese número.")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad += 1
        return True

    def listar(self):
        if self.esta_vacia():
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):
            marca = " ← TOPE" if i == self.cantidad - 1 else (" ← FONDO" if i == 0 else "")
            print(f"  [{i}] {self.datos[i]}{marca}")

    def desapilar(self):
        if self.esta_vacia():
            return None
        pasajero = self.datos[self.cantidad - 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return pasajero

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.datos[self.cantidad - 1]

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        auxiliar = MiPila(self.capacidad)
        encontrado = None
        while not self.esta_vacia():
            pasajero = self.desapilar()
            if pasajero.numero == numero:
                encontrado = pasajero
                break
            auxiliar.apilar(pasajero)
        while not auxiliar.esta_vacia():
            self.apilar(auxiliar.desapilar())
        return encontrado

    def copiar(self):
        copia = MiPila(self.capacidad)
        for i in range(self.cantidad):
            copia.apilar(self.datos[i])
        return copia

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
