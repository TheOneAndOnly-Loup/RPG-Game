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
        self.health += 15

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
print("You enter an arena and see a goblin standing in front of you.")

while goblin_char.is_alive and hero.is_alive:
    print(f"{hero_name}'s Health: {hero.health}/100")
    print(f"{goblin_char.name}'s Health: {goblin_char.health}/75")
    menu_choice = int(input("What do you do? \n1. Attack \n2. Heal\n\n: "))
    if menu_choice == 1:
        hero.attack(goblin_char)
        print(f"\nYou attack the goblin with your sword. It does {hero.strength} damage.")
    if menu_choice == 2:
        hero.heal()
        print("\nYou regain 10 HP points.")
    sleep(0.5)

    goblin_char.attack(hero)
    print(f"\nThe goblin now attacks you. It does {goblin_char.strength} damage.\n")
    print("--------------------------------------------------")

print("You successfully defeated the goblin. However, you see a dark figure emerging from the shadows. It's a dragon!")

while dragon_char.is_alive and hero.is_alive:
    print(f"{hero_name}'s Health: {hero.health}/100")
    print(f"{dragon_char.name}'s Health: {dragon_char.health}/75")
    menu_choice = int(input("What do you do? \n1. Attack \n2. Heal\n\n: "))
    if menu_choice == 1:
        hero.attack(dragon_char)
        print(f"\nYou attack the dragon with your sword. It does {hero.strength} damage.")
    if menu_choice == 2:
        hero.heal()
        print("\nYou regain 10 HP points.")
    sleep(0.5)

    dragon_char.attack(hero)
    print(f"\nThe dragon now attacks you. It does {dragon_char.strength} damage.\n")
    print("--------------------------------------------------")


