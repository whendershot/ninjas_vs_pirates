class Actor:
    """
    """

    current_actors = []

    def __init__( self, name ):
        self.name = name
        self.strength = 1
        self.speed = 1
        self.health = 1
        Actor.current_actors.append( self )

        self.attack_cooldown_timer = self.speed

    def __repr__( self ): 
        return f"{self.name}, Health: {self.health}, Attack cooldown: {self.attack_cooldown_timer}"

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , other):
        other.health -= self.strength
        return self
