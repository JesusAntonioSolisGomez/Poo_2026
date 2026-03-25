###
## Excepciones basicas  | Frutraas y precios

#Parte 3 
frutas = ["manzana", "pera", "uva"]
precios = {"manzana": 10, "pera": 8, "uva": 15}

try:
    idx = int(input("Indice (0-2): "))
    print(f"Fruta: {frutas[idx]}")

    clave = input("Nombre de fruta para ver precio: ")
    print(f"Precio: ${precios[clave]}")

except IndexError as e:
    print(f" Índice inválido: {e}")

except KeyError as e:
    print(f" Fruta no encontrada: {e}")

except ValueError:
    print(" El índice debe ser un número.")