import random

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        random_block = random.randint(0, self.max_block)
        print(random_block)
        return random_block

if __name__ == "__main__":
    ability_1 = Armor("Shield", 25)
    print(ability_1.name)
    print(ability_1.max_block)
    ability_1.block()
