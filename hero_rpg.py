#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self,name, health, power):
        self.health = health
        self.power = power
        self.name = name

    def attack(self, other_character):
        other_character.health -=self.power
        print(" The {} does {} damage to the {}.".format(self.name, self.power, other_character.name, ))
        
        if other_character.health <= 0:
            if other_character.name != zombie.name:
                print(f'The {other_character.name} is dead.')
            else:
                print(f'The {other_character.name} is dead. But death does not stop {other_character.name}')

    def alive(self):
        if self.health>0:
            return True
        else:
            return False
    
    def print_status (self):
        print("The {} has {} health and {} power.".format( self.name,self.health, self.power))

class Hero(Character):
    pass

class Goblin(Character):
    pass


class Zombie(Goblin):
    
    def alive(self):
        return True


hero = Hero("hero",10,8)
goblin = Goblin("goblin",5,2)
zombie = Zombie('zombie',0,1)
def main():
    while goblin.alive() or zombie.alive() and hero.alive():
        hero.print_status()

        zombie.print_status()
        
        print()
        print("What do you want to do?")
        print("1. fight vilian")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(zombie)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0 or zombie.alive():
            zombie.attack(hero)


main()
