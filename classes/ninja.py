from classes.actor import Actor

class Ninja(Actor):

    def __init__( self , name ):
        super().__init__(name)
        self.strength = 10
        self.speed = 5
        self.health = 100
