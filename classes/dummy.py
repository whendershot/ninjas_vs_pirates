from classes.actor import Actor, HealthState

class Dummy(Actor):

    current_dummies = None

    def __init__(self, name):
        super().__init__(name)
        self.strength = 1
        self.speed = 1
        self.health = 100

        if not current_dummie:
            Dummy.current_dummies.append(self)

    def attack(self, defender):        
        if super().attack(defender, self.strength):
            print(f"{self.name}: Bumps into {defender.name}!")

    def defend(self, attacker, attack_strength):
        super().defend(attacker, attack_strength)
        print(f"{self.name}: Takes a beating from {attacker.name}!")
        
        # if self.health_state == HealthState.IS_DYING:
        #     self.health_state = HealthState.IS_DEAD
        #     Dummy.current_dummies.remove(self)        
        # elif self.health <= 0:
        #     self.health_state = HealthState.IS_DYING