from classes.actor import Actor

class Ninja(Actor):

    def __init__(self, name):
        super().__init__(name)
        self.strength = 20
        self.speed = 5
        self.health = 100

    def attack(self, other):
        if super().attack(other):
            print(f"A whisper on the wind? {self.name} attacks {other.name}")