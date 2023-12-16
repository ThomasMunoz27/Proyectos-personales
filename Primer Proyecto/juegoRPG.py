import funcionesRPG as function
#Mensaje de bienvenida
print("Bienvenido al Juego RPG. \n Elije a tu personaje")
while True:
    try:
        character_selection = int(input(" (1) Mago\n (2) Paladin \n :"))
        if character_selection == 1:
            from personajes import Mago
            name = function.valid_name("Has elejido un Mago. Ponle un nombre: ")
            character = Mago(name)
            print(f"{character.name} es un {character.__class__.__name__}")
            break

        if character_selection == 2:
            from personajes import Paladin
            name = function.valid_name("Has elejido un Paladín. Ponle un nombre: ")
            character = Paladin(name)
            print(f"{character.name} es un {character.__class__.__name__}")
            break
    except ValueError:
        print("Ingrese un número válido\n")
from personajes import Bandido
enemy = Bandido()
print(f"Te has encontrado con un {enemy.__class__.__name__} y te ataca.")
character.attacks_menu(enemy)

print("Has sobrevivido al combate")