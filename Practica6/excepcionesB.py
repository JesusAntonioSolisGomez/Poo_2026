###
## Excepciones basicas  | Captura de multiples excepciones

#Parte 2 

print("="*50)
print("Parte 2: Acceso a lista de colores")
print("="*50)

#Creamos una lista de colores
colores = ["rojo", "verde", "azul", "amarillo"]
print(f"lista de colores: {colores} (indice 0, 1, 2, 3)")
try:
    indice = int(input("Que color quieres acceder? (0-3): "))
    print(f"El color seleccionado es: {colores[indice]}")
    
except ValueError as e:
    print(f"ValueError: {e}")
        
except IndexError as e:
        print(f"IndexError: {e}")
        print("Error: El indice debe estar entre 0 y 3.")
        
finally:
    print("Fin del programa.")
    