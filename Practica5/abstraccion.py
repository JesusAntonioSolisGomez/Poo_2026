from abc import ABC, abstractmethod

#Clase abstracta

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass
    
class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"
    
    #usar las clases
    
perro = Perro()
gato = Gato()

print(perro.hablar())
print(gato.hablar())
