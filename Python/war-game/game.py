# Character (parent class - all common attributes - hero and villain)
# Hero: Controlled by the end user
# Villain: Adversary

import random 
class Character():
    def __init__(self, name, health, level):
        self.__name = name 
        self.__health = health
        self.__level = level

    
    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    def get_level(self):
        return self.__level
    
    def show_details(self):
        return f"Name: {self.get_name()}\nHealth: {self.get_health()}\nLevel: {self.get_level()}"
    
    def attack_received(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0
    
    def attack(self, target):
        damage = random.randint(self.get_level() * 2, self.get_level() * 4) # based on the level
        target.attack_received(damage)
        print(f"{self.get_name()} attacked {target.get_name()} and caused {damage} damage")

    
class Hero(Character):
    def __init__(self, name, health, level, skill):
        super().__init__(name, health, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill
    
    def show_details(self):
        return f"{super().show_details()}\nSkill: {self.get_skill()}\n"
    
    def special_attack(self, target):
        damage = random.randint(self.get_level() * 5, self.get_level() * 8) # based on the level
        target.attack_received(damage)
        print(f"{self.get_name()} used the special attack {self.get_skill()} in {target.get_name()} and caused {damage} damage")

class Villain(Character):
    def __init__(self, name, health, level, variety):
        super().__init__(name, health, level)
        self.__variety = variety

    def get_variety(self):
        return self.__variety 
    
    def show_details(self):
        return f"{super().show_details()}\nSkill: {self.get_variety()}\n"


class Game:
    """Orchestrator class"""
    def __init__(self) -> None:
        self.hero = Hero(name= "superman", health=100, level=5, skill="Strength")
        self.villain = Villain(name= "Lex Luthor", health=100, level=5, variety="Super-genius")
    
    def initiate_battle(self):
        """Manage turns"""
        print("The battle begins")
        while self.hero.get_health() > 0 and self.villain.get_health() > 0:
            print("\n Characters details: ")
            print(self.hero.show_details())
            print(self.villain.show_details())

            input("Press enter to attack...")
            choice = input("Choose (1- Normal attack, 2- Special attack): ")

            if choice == '1':
                self.hero.attack(self.villain)
            elif choice == '2':
                self.hero.special_attack(self.villain)
            else:
                print("Invalid choice. Choose again")

            if self.villain.get_health() > 0:
                # Villain attacks the hero
                self.villain.attack(self.hero)

        if self.hero.get_health() > 0:
            print("\nCongrats, you won the battle!")
        else:
            print("\nDamn, you lost the battle!")

game = Game()
game.initiate_battle()