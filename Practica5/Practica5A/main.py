from Vaca import Vaca
from Creeper import Creeper
from Enderman import Enderman

def main():
    mobs = [
        Vaca("Bessie", 10),
        Creeper("Explosi", 20),
        Enderman("Tall Boi", 40),
    ]

    for mob in mobs:
        mob.presentarse()

if __name__ == "__main__":
    main()