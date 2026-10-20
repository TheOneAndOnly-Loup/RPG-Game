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
        if self.health < 0:
            self.is_alive = False

class Player(GameCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.health = 100
        self.strength = 10
    def heal(self):
        self.health += 10

class Enemy(GameCharacter):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.strength = 10

class Goblin(Enemy):
    def __init__(self, health):
        super().__init__(self, health)
        self.name = "Goblin"

class Dragon(Enemy):
    def __init__(self, health):
        super().__init__(self, health)
        self.name = "Dragon"

class ScoreCounter:
    def __init__(self):
        self.score = 0
    def add_score(self, amount):
        self.score += amount
    def remove_score(self, amount):
        self.score -= amount

hero_name = input("What is your name? ")
hero = Player(hero_name)
goblin_char = Goblin(50)
dragon_char = Dragon(75)

print("-------------------------\n\nRPG GAME\n\n-------------------------\n")
print("You enter an arena and see a goblin standing in front of you. What do you do?")
while goblin_char.is_alive() or hero.is_alive():
    print(f"""{hero_name}'s Health: {hero.health}/100
          \n""")