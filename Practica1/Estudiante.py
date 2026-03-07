# Esta es la clase Estudiante
class Estudiante:

    # Aqui va el constructor de la clase
    def __init__(self,nombre,edad,carrera,):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

        # Metodo para agregar calificaciones
        def setCalificaciones(self, calificacion):
            self.calificaciones.append(calificacion)

            def getNombre(self):
                return self.nombre

        # Metodo para calcular el promedio de las calificaciones
        def getPromedio(self):
            if len(self.calificaciones) == 0:
                return 0
            return sum(self.calificaqciones) / len(self.calificaciones)
    
    # Metodo para mostrar la informacion del estudiante
    def mostrarInformacionUsuario(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.cafrrera}."
    
    #Crear los objetos (instancia) de la clase
    estudiante1 = Estudiante("Paco",30;"Ing. en Sistemas")
    estudiante2 = Estudiante("Carmen",25;"In, en Industrial")
    estudiante3 = Estudiante("Ramon",20;"Ing. en Electronica")

    print(estudiante1.mostrarInformacionUsuario())
    
    estuandiante1.setCalificaciones(75)
    estudiante1.setCalificaciones(98)

print(f"La calificación del {estudiante1.getNombre} es: {estudiante1.mostrarPromedio()}")

