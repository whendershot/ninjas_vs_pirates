from classes.actor import Actor

class Pirate(Actor):

    def __init__( self , name ):
        super().__init__(name)
        self.strength = 15
        self.speed = 3
        self.health = 100