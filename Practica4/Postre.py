from Platillo import Platillo

class Postre(Platillo):
    def __init__(self, nombre, precio, es_sin_gluten):
        super().__init__(nombre, precio)
        self.es_sin_gluten = es_sin_gluten

    def tipo(self):
        if self.es_sin_gluten:
            gluten = "Sí"
        else:
            gluten = "No"
        print(f"Tipo: Postre - Sin gluten: {gluten}")