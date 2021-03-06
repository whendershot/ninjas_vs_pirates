from classes.actor import Actor
from classes.ninja import Ninja
from classes.pirate import Pirate

import random
import time

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()

jack_sparrow.attack(michelangelo)
michelangelo.show_stats()

print(Actor.current_actors)

pirates = []
ninjas = []

ninjas.append(Ninja("Raphael"))
ninjas.append(Ninja("Donatello"))
ninjas.append(Ninja("Leonardo"))
ninjas.append(michelangelo)

pirates.append(Pirate("Typhoid Mary"))
pirates.append(Pirate("Sick Sam"))
pirates.append(Pirate("Rowdy Mike"))
pirates.append(jack_sparrow)

#Game loop
frame = 0

while (len(Pirate.current_pirates) > 0 and len(Ninja.current_ninjas) > 0):
    frame += 1    
    # for pirate in list(pirates):
    #     try:
    #         defender = random.choice(ninjas)
    #     except IndexError:
    #         defender = Actor("Dummy")
    #     if defender.is_dying:
    #         ninjas.remove(defender)
    #     else:
    #         pirate.attack(defender)
    #     pirate.update()

    # for ninja in list(ninjas):
    #     try:
    #         defender = random.choice(pirates)
    #     except IndexError:
    #         defender = Actor("Dummy")
    #     if defender.is_dying:
    #         pirates.remove(defender)
    #     else:
    #         ninja.attack(defender)
    #     ninja.update()
    
    for attacker in list(random.sample(population=Actor.current_actors, k=len(Actor.current_actors))):
        defender = None
        try:
            
            if isinstance(attacker, Pirate):
                defender = random.choice(Ninja.current_ninjas)
            else:
                defender = random.choice(Pirate.current_pirates)
        except IndexError:
            print(f"Team {type(attacker)} has won!")
            break

        attacker.attack(defender)
        attacker.update()

    print(f"End of frame {frame}")
    print(f"Pirates: {Pirate.current_pirates}")
    print(f"Ninjas: {Ninja.current_ninjas}")
    time.sleep(1)

print(f"\nFinal results:")
print(f"Pirates: {pirates}")
print(f"Ninjas: {ninjas}")
