import random

class Team:
    def __init__: (self, name, heroes):
        self.name = name
        self.heroes = heroes
        self.kills = []
        self.deaths = []
    
    def add_hero(self, heroes):
        self.heroes.append(heroes)
    
    def remove_hero(self, heroes):
        self.heroes.pop(heroes)
    
    def view_all_heroes(self, heroes):
        print(self.heroes)
    
    def add_kill(self, kill):
        self.kills.append(kill)

    def add_death(self, death):
        self.deaths.append(death)
