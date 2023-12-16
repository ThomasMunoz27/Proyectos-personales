import time
import random
class Characters:

    # Carácteristicas generales #
    def __init__(self, name="", alive=True, money=150, ps=100):
        self.name = name
        self.alive = alive
        self.money = money
        self.ps = ps

        

class Mago(Characters):
    def __init__(self, name="", alive=True, money=150, dmg=5, mag_dmg=25, armor=5, mag_armor=5, mana = 100):
        super().__init__(name, alive, money)
        self.dmg = dmg
        self.mag_dmg = mag_dmg
        self.armor = armor
        self.mag_armor = mag_armor
        self.mana = mana

    #Métodos de estado 

    def game_over(self):
        #Si los ps del personaje llegan a 0 se interrumpe la ejecución, mostrando un mensaje de derrota
        if self.ps <= 0:
            self.alive = False
            if self.alive == False:
                print(f"{self.name} ha fallecido.")
                raise SystemExit("Game Over.")

    #Métodos de combate
    def attacks_menu(self, enemy):
        while enemy.ps > 0:
            #chequea antes de cada turno que el persoanje esté vivo
            self.game_over()
            print(f"Elije un ataque (Mana: {self.mana}/100). \n\n (1)Golpe de bastón \n (2)Chorro de agua (15 mana) \n (3)Aumento de fe (10 mana) \n (4)Flamas infernales (50 mana)")
            while True:
                try:
                    attack = int(input(": "))
                    time.sleep(1)

                    if attack == 1:
                        dmg = self.dmg - enemy.armor
                        if dmg <= 0:
                            enemy.ps -= 0

                        else:
                            enemy.ps -= dmg

                    elif attack == 2:
                        if self.mana >= 15:
                            self.mana -= 15
                            enemy.ps -= self.mag_dmg
                        else:
                            print("Maná insuficiente. Fallaste el ataque")

                    elif attack == 3:
                        if self.mana >= 10:
                            self.mana -= 10
                            self.mag_dmg += 10
                        else:
                            print("Maná insuficiente. Fallaste el ataque")

                    elif attack == 4:
                        if self.mana >= 50:
                            self.mana -= 50
                            enemy.ps -= (self.mag_dmg * 2)
                        else:
                            print("Maná insuficiente. Fallaste el ataque")

                    else:
                        print("Número de ataque inválido")
                        break
                    
                    print(f"Vida del enemigo: {enemy.ps}")
                    if enemy.ps <= 0:
                        break
                    print(f"El {enemy.__class__.__name__} te ataca")
                    self.ps -= enemy.dmg - self.armor
                    time.sleep(1)
                    print(f"Tu vida bajó a {self.ps}")
                    time.sleep(1)
                    break
                except ValueError:
                        print("Número de ataque inválido")


class Paladin(Characters):
    def __init__(self, name="", alive=True, money=150, dmg=10, mag_dmg=0, armor=20, mag_armor=20):
        super().__init__(name, alive, money, ps=150)
        self.dmg = dmg
        self.mag_dmg = mag_dmg
        self.armor = armor
        self.mag_armor = mag_armor

    #Métodos
    def game_over(self):
        if self.alive == False:
            print(f"{self.name} ha fallecido.")
            raise SystemExit("Game Over.")
            

    def check_ps(self):
        if self.ps <= 0:
            self.alive = False

    #Clase enemigo
class Bandido(Characters):
    def __init__(self, name="", alive=True, money=150, ps=100, dmg = 15, armor = 10):
        super().__init__(name, alive, money, ps)
        self.dmg = dmg
        self.armor = armor