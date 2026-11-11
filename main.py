from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ingresar un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito", "12A"),
        Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "03C"),
        Pasajero(1009, "Luis", "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto", "0934567890", 16, "2026-11-20", "Quito", "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima", "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar lineal   6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()
        if op == "1":
            if pila.apilar(leer_pasajero()): print("  Pasajero apilado correctamente.")
        elif op == "2": pila.listar()
        elif op == "3":
            p = pila.desapilar()
            print("  Salió: " + str(p) if p else "  La pila está vacía.")
        elif op == "4":
            p = pila.ver_tope()
            print("  Tope: " + str(p) if p else "  La pila está vacía.")
        elif op == "5":
            n = leer_entero("  Número a buscar: "); pos = pila.buscar(n)
            print(f"  Encontrado en posición {pos}: {pila.datos[pos]}" if pos != -1 else "  No existe.")
        elif op == "6":
            n = leer_entero("  Número: "); d = input("  Nuevo destino: ").strip(); a = input("  Nuevo asiento: ").strip().upper()
            print("  Modificado." if pila.modificar(n, d, a) else "  No se encontró el pasajero.")
        elif op == "7":
            n = leer_entero("  Número a eliminar: "); p = pila.eliminar_por_numero(n)
            print("  Eliminado: " + str(p) if p else "  No existe.")
        elif op == "8":
            copia = pila.copiar(); print("  Copia de la pila:"); copia.listar()
        elif op == "9": print(f"  Longitud: {pila.longitud()} · Vacía: {'Sí' if pila.esta_vacia() else 'No'}")
        elif op == "C":
            for p in datos_prueba(): pila.apilar(p)
            print("  Datos de prueba cargados (sin duplicar números).")
        elif op == "0": break
        else: print("  Opción no válida.")


def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        print(" 10. Búsqueda binaria              11. Ordenar ascendente")
        print(" 12. Ordenar descendente           13. Registrar reserva")
        print(" 14. Listar reservas")
        op = input("Opción: ").strip().upper()
        if op == "1":
            if cola.encolar(leer_pasajero()): print("  Pasajero encolado correctamente.")
        elif op == "2": cola.listar()
        elif op == "3":
            p = cola.desencolar(); print("  Salió: " + str(p) if p else "  La cola está vacía.")
        elif op == "4":
            p = cola.ver_frente(); print("  Frente: " + str(p) if p else "  La cola está vacía.")
        elif op == "5":
            n = leer_entero("  Número a buscar: "); pos = cola.buscar(n)
            print(f"  Encontrado en posición {pos}: {cola.datos[pos]}" if pos != -1 else "  No existe.")
        elif op == "6":
            n = leer_entero("  Número: "); d = input("  Nuevo destino: ").strip(); a = input("  Nuevo asiento: ").strip().upper()
            print("  Modificado." if cola.modificar(n, d, a) else "  No se pudo modificar (no existe o asiento ocupado).")
        elif op == "7":
            n = leer_entero("  Número a eliminar: "); p = cola.eliminar_por_numero(n)
            print("  Eliminado: " + str(p) if p else "  No existe.")
        elif op == "8":
            copia = cola.copiar(); print("  Copia de la cola:"); copia.listar()
        elif op == "9": print(f"  Longitud: {cola.longitud()} · Vacía: {'Sí' if cola.esta_vacia() else 'No'}")
        elif op == "10":
            n = leer_entero("  Número para búsqueda binaria: "); p = cola.busqueda_binaria(n)
            print("  Encontrado: " + str(p) if p else "  No existe.")
        elif op == "11": cola.ordenar_asc()
        elif op == "12": cola.ordenar_desc()
        elif op == "13":
            p = leer_pasajero(); ok, mensaje = cola.reservar(p); print("  " + mensaje)
        elif op == "14": cola.listar_reservas()
        elif op == "C":
            for p in datos_prueba(): cola.encolar(p)
            print("  Datos de prueba cargados (sin duplicar números).")
        elif op == "0": break
        else: print("  Opción no válida.")


def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1": menu_pila()
        elif op == "2": menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else: print("Opción no válida.")


if __name__ == "__main__":
    main()
