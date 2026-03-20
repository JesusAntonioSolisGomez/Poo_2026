from Pico import Pico
from Espada import Espada
from Pala import Pala
from Arco import Arco

def main():
    herramientas = [
        Pico("diamante", 3),
        Espada("hierro", 2),
        Pala("madera", 2),
        Arco("oro", 3, 2)
    ]

    objetivos = ["mena de diamante", "Creeper", "arena", "Zombie"]

    for h, obj in zip(herramientas, objetivos):
        while not h.rota:
            print(h.usar(obj))
            h.estado()
        print()

if __name__ == "__main__":
    main()