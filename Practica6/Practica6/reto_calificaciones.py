# --- Excepción personalizada ---
class CalificacionFueraDeRangoError(Exception):
    def __init__(self, calificacion):
        super().__init__(f"Calificación inválida: {calificacion}. Debe estar entre 0 y 100.")
        self.calificacion = calificacion


# --- Función para pedir enteros ---
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print(" Ingresa un número válido.")


# --- Programa principal ---
contador = 0

try:
    nombre_archivo = input("Nombre del archivo (.txt): ")

    while True:
        nombre = input("Nombre del estudiante (o 'salir' para terminar): ")
        
        if nombre.lower() == "salir":
            break

        try:
            calificacion = pedir_entero("Calificación (0-100): ")

            # Validación
            if not (0 <= calificacion <= 100):
                raise CalificacionFueraDeRangoError(calificacion)

            # Guardar en archivo
            with open(nombre_archivo, "a", encoding="utf-8") as archivo:
                archivo.write(f"{nombre} - {calificacion}\n")

            contador += 1
            print(" Registro guardado\n")

        except CalificacionFueraDeRangoError as e:
            print(f" {e}\n")

except FileNotFoundError:
    print(" El archivo no existe.")

except PermissionError:
    print(" No tienes permisos para escribir en ese archivo.")

except Exception as e:
    print(f" Error inesperado: {e}")

finally:
    print(f"\n Total de estudiantes registrados: {contador}")
    print("Programa finalizado.")