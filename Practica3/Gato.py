from Animal import Animal

class Gato(Animal.Animal):
    
    def hablar(self):
        print(f"{self.nombre}: ¡Miau!")