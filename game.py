from time import sleep

class GameCharacter:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.is_alive = True
    def attack(self, target):
        damage = self.strength
        target.take_damage(damage)
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.is_alive = False

class Player(GameCharacter):
    def __init__(self, name):
        super().__init__(name, 100, 10)
    def heal(self):
        self.health += 20

class Enemy(GameCharacter):
    def __init__(self, name, health):
        super().__init__(name, health, 10)

class Goblin(Enemy):
    def __init__(self, health):
        super().__init__("Goblin", health)

class Dragon(Enemy):
    def __init__(self, health):
        super().__init__("Dragon", health)


hero_name = input("What is your name? ")
hero = Player(hero_name)
goblin_char = Goblin(75)
dragon_char = Dragon(75)


print("-------------------------\n\nRPG GAME\n\n-------------------------\n")
print("You enter an arena and see an enemy standing in front of you.")

while True:
    if goblin_char.is_alive:
        active_enemy = goblin_char
    elif dragon_char.is_alive and hero.is_alive and not goblin_char.is_alive:
        print("You successfully defeated the goblin. However, you see a dark figure emerging from the shadows. It's a dragon!")
        active_enemy = dragon_char
    elif not hero.is_alive:
        quit(f"\nThe {active_enemy.name} killed {hero_name}.")
    else:
        break

    print(f"{hero_name}'s Health: {hero.health}/100")
    print(f"{active_enemy.name}'s Health: {active_enemy.health}/75")
    
    menu_choice = input("What do you do? \n1. Attack \n2. Heal\n\n: ")
    try:
        if int(menu_choice) == 1:
            hero.attack(active_enemy)
            print(f"\nYou attack the {active_enemy.name.lower} with your sword. It does {hero.strength} damage.")
        elif int(menu_choice) == 2:
            hero.heal()
            print("\nYou regain 20 HP points.")
            sleep(0.5)
        else:
            print("Invalid input. Please enter a valid choice.")
            continue
    except:
        print("Invalid input. Please enter a valid choice.")
        continue
    
    active_enemy.attack(hero)
    print(f"\nThe {active_enemy.name} now attacks you. It does {active_enemy.strength} damage.\n")
    print("--------------------------------------------------")

print("Congratulations! You successfully slayed both enemies. You make your way out of the arena.")