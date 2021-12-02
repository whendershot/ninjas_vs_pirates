from classes.actor import Actor

class Pirate(Actor):

    def __init__(self, name):
        super().__init__(name)
        self.strength = 15
        self.speed = 3
        self.health = 100

    def attack(self, other):        
        if super().attack(other):
            print(f"{self.name}: Yarg, git sum {other.name}!")
