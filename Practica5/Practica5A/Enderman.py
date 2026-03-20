from mob import Mob

class Enderman(Mob):

    def hacer_sonido(self) -> str:
        return "Ruidos distorsionados"

    def comportamiento(self) -> str:
        return "neutral"

    def moverse(self) -> str:
        return "Se teletransporta"