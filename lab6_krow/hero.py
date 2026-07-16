import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.weapons = []
        self.deaths = []
        self.kills = []

    def battle(self, opponent):
     #chooses a random winner between 2 heroes
        print(random.choice([self.name, opponent.name]))

    
    def add_ability(self, ability): # adds an ability to a hero's list of abilities
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack() # total_damage = total_damage + ability.attack()
        print(total_damage)
        return total_damage
    
    def add_armor(self, armor): # adds an armor to a hero's list of abilities
        self.armors.append(armor)
    
    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        print(total_block)
        return total_block
    
    def take_damage(self, damage):
        blocked = self.defend()
        actual_damage = max(damage - blocked, 0)
        self.current_health -= actual_damage # self.current_health = self.current_health - actual_damage
        if self.current_health < 0:
            self.current_health = 0
        return actual_damage
    
    def add_weapon(self, weapon):
        self.weapons.append(weapon)
    
    def add_kill(self, kill)
        self.kills.append(kill)
    
    def add_death(self, death)
        self.deaths.append(death)






if __name__ == "__main__":
    my_hero = Hero("Giorno Giovanna", 150)
    #print(my_hero.name)
    #print(my_hero.current_health)
    #my_opponent = Hero("Diavolo", 200)
    my_hero.battle(my_opponent)
    my_hero.add_armor(Armor("Gloves", 5))
    my_hero.add_armor(Armor("Cape", 10))
    my_hero.take_damage(25)
    print(my_hero.current_health)

