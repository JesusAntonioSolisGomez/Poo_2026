from Comida import Comida
from Bebida import Bebida
from Postre import Postre

# Crear objetos
comida1 = Comida("Tacos al pastor", 85.0, "Principal")
bebida1 = Bebida("Limonada", 35.0, "Fria")
postre1 = Postre("Flan", 45.0, False)

# Mostrar información
comida1.mostrar_info()
comida1.tipo()
print("---")

bebida1.mostrar_info()
bebida1.tipo()
print("---")

postre1.mostrar_info()
postre1.tipo()