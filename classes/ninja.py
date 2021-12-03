from classes.actor import Actor, HealthState

class Ninja(Actor):

    current_ninjas = []

    def __init__(self, name):
        super().__init__(name)
        self.strength = 20
        self.speed = 5
        self.health = 100
        
        Ninja.current_ninjas.append(self)

    def attack(self, defender):
        if super().attack(defender, self.strength):
            print(f"A whisper on the wind? {self.name} attacks {defender.name}")

    def defend(self, attacker, attack_strength):
        super().defend(attacker, attack_strength)
        print(f"{self.name}: I was careless about {attacker.name}...")
        
        if self.health_state == HealthState.IS_DYING:
            self.health_state = HealthState.IS_DEAD
            Ninja.current_ninjas.remove(self)
        elif self.health <= 0:
            self.health_state = HealthState.IS_DYING