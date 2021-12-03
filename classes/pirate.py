from classes.actor import Actor, HealthState

class Pirate(Actor):

    current_pirates = []

    def __init__(self, name):
        super().__init__(name)
        self.strength = 15
        self.speed = 3
        self.health = 100

        Pirate.current_pirates.append(self)

    def attack(self, defender):        
        if super().attack(defender, self.strength):
            print(f"{self.name}: Yarg, git sum {defender.name}!")

    def defend(self, attacker, attack_strength):
        super().defend(attacker, attack_strength)
        print(f"{self.name}: Curse ye {attacker.name}!")
        
        if self.health_state == HealthState.IS_DYING:
            self.health_state = HealthState.IS_DEAD
            Pirate.current_pirates.remove(self)        
        elif self.health <= 0:
            self.health_state = HealthState.IS_DYING