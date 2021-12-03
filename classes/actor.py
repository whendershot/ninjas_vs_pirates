from enum import Enum, auto

class HealthState(Enum):
    IS_DYING = auto()
    IS_DEAD = auto()
    IS_HEALTHY = auto()

class Actor():
    """
    """
    current_actors = []

    def __init__(self, name):
        self.name = name
        self.strength = 1
        self.speed = 1
        self.health = 1
        self.health_state = HealthState.IS_HEALTHY
        self.attack_cooldown_timer = 0

        Actor.current_actors.append(self)

    def __repr__(self): 
        return f"{self.name}, Health: {self.health}, Attack cooldown: {self.attack_cooldown_timer}"

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, defender, attack_strength):
        if self.attack_cooldown_timer <= 0:
            defender.defend(self, attack_strength)
            return True
        return False

    def defend(self, attacker, attack_strength):
        self.health -= attack_strength

    def update(self):
        self.attack_cooldown_timer = (self.attack_cooldown_timer + 1) % self.speed
        
        if self.health_state == HealthState.IS_DYING:
            Actor.current_actors.remove(self)        
        elif self.health <= 0:
            self.HEALTH_STATE = HealthState.IS_DYING
