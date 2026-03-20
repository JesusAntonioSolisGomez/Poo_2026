from mob import Mob

class Vaca(Mob):

    def hacer_sonido(self) -> str:
        return "Muuuu"

    def comportamiento(self) -> str:
        return "pasivo"

    def moverse(self) -> str:
        return "Camina lentamente por el prado"