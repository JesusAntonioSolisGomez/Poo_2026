from mob import Mob

class Creeper(Mob):

    def hacer_sonido(self) -> str:
        return "...Ssssss"

    def comportamiento(self) -> str:
        return "agresivo"

    def moverse(self) -> str:
        return "Corre directamente hacia el jugador"