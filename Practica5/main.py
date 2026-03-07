from Guerrero import Guerrero
from Mago import Mago
from Arquero import Arquero

# Crear objetos
guerrero1 = Guerrero("Thorin", 8, "Hacha")
mago1 = Mago("Gandalf", 15, "Bola de fuego")
arquero1 = Arquero("Legolas", 10, 30)

# Guerrero
guerrero1.presentarse()
guerrero1.usar_habilidad()
print("---")

# Mago
mago1.presentarse()
mago1.usar_habilidad()
print("---")

# Arquero
arquero1.presentarse()
arquero1.usar_habilidad()