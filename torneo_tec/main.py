from Competidor import Competidor
from Observador import Observador

# Crear un competidor
carlos = Competidor("Carlos Mendez", "21100123", "avanzado", "Team Overflow")

carlos.mostrar_perfil()
carlos.ganar_puntos(50)
carlos.perder_puntos(20)

print()  # Separación visual

# Crear un observador
ana = Observador("Ana Torres", "21100456", "principiante")

ana.ver_partida()
ana.ver_partida()

print()  # Separación visual

ana.mostrar_perfil()