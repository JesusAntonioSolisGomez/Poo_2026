class Mascota:
    def __init__(self, nombre, tipo, edad, nivelFelicidad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.nivelFelicidad = nivelFelicidad

    def alimentar(self):
        self.nivelFelicidad = self.nivelFelicidad + 10
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100

    def jugar(self):
        self.nivelFelicidad = self.nivelFelicidad + 20
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100

    def mostrarEstado(self):
        return f"{self.nombre} es un {self.tipo} con felicidad: {self.nivelFelicidad}"

    def esFeliz(self):
        return self.nivelFelicidad > 70


# Crear mascota1
mascota1 = Mascota("Bobby", "Perro", 3, 50)

print(mascota1.mostrarEstado())
print(f"Es feliz? {mascota1.esFeliz()}")

print(f"Alimentando a {mascota1.nombre}...")

mascota1.alimentar()
print(mascota1.mostrarEstado())

print(f"Jugando con {mascota1.nombre}...")

mascota1.jugar()
print(mascota1.mostrarEstado())
print(f"Es feliz? {mascota1.esFeliz()}")

print("------------------------------------------------")

# Crear mascota2
mascota2 = Mascota("Michi", "Gato", 2, 30)

print(mascota2.mostrarEstado())
print(f"Es feliz? {mascota2.esFeliz()}")

print(f"Alimentando a {mascota2.nombre}...")

mascota2.alimentar()
print(mascota2.mostrarEstado())

print(f"Jugando con {mascota2.nombre}...")

mascota2.jugar()
print(mascota2.mostrarEstado())
print(f"Es feliz? {mascota2.esFeliz()}")



