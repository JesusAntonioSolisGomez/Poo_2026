#Clase base
class Animal:
    #creamos el constructor de la clase animal
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def describir(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años.")
        
    def hablar(self):
        print("...")
   
