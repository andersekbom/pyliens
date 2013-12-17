### A reenactment of James Cameron's Aliens in Python ###

from sys import exit
from random import randint
from time import sleep

win = False

### Classes ##################################################

### Maybe I'll need this one day
class Player(object):
    def __init__(self):
        pass

### Quick, sleek and pointy teeth
class Alien(object):

    def __init__(self,name):
        self.name = name
        self.health  = 100

    def bite(self, weapon):
        fight(alien, marine, weapon)

### Large, lumbering and with guns
class Marine(object):

    def __init__(self, name, rounds):
        self.name = name
        self.rounds = rounds
        self.initRounds = rounds
        self.weapon = ""

    def fire(self, weapon):
        marine.rounds -= 1
        fight(marine, alien, weapon)

### Armory ##################################################

#weapons = {
#    'Pulse rifle' : ''

### Functions ###############################################

def checkForHit():

    attackPoint = randint(1,9)
    defendPoint = randint(1,9)    

    if attackPoint > defendPoint:
        hit = True
    else:
        hit = False
    return hit

def fight(attacker, defender, weapon):

    hit = checkForHit()

    if attacker == alien and hit:
        print "Alien attacks with %s and hits!\n" % weapon,
    elif attacker == alien and not hit:
        print "Alien attacks with %s but misses!\n" % weapon,
    elif attacker == marine and hit:
        print "Marine fires %s and hits!\n" % weapon,
        alien.health -= 50
    elif attacker == marine and not hit:
        print "Marine fires %s but misses!\n" % weapon,
    else:
        exit

    print "Alien has %s health, marine har %s rounds left in gun.\n" % (alien.health,marine.rounds)

def chooseSides():
    print "Which side do you want to play?"
    print "1: Alien"
    print "2: Marine"
    side = raw_input("> ")
    if side == "1":
        print "Sorry, they're too sacry."
        chooseSides()
    elif side == "2":
        return side
    else:
            print "What?"
            chooseSides()

def chooseWeapon():
    print "Which gun do you want to use?"
    print "1: Pulse rifle - 50dmg, 75% chance to hit."
    print "2: Grenade launcher - 100dmg, 50% chance to hit."
    weapon = int(raw_input("> "))
    if weapon == 1:
        marine.weapon = "pulse rifle"
    elif weapon == 2:
        marine.weapon = "grenade launcher"


def ticker(ticks):
    while ticks > 0:
        print " "
        ticks -= 1
        sleep(2)

def playAgain():
    playAgain = raw_input("\nPlay again? (y/n)")
    if playAgain == "y":
            runGame()
    elif playAgain == "n":
        print "Goodbye!"
    else:
        print "What?"
        playAgain()

def runGame():

    alien.health = 100
    marine.rounds = marine.initRounds

    side = chooseSides()
    
    side = 1
    if side == "1":
        print "You're the Alien!"
    elif side == "2":
        print "You're the Marine!"
        chooseWeapon()
    else:
        print "ERROR 1"
        

    while marine.rounds > 0:
        marine.fire(marine.weapon)
        if alien.health <= 0:
            print "\n### Marine wins!"
            break
        elif marine.rounds == 0:
            alien.bite("claws")
            print "\n### Alien wins!"
            break
    playAgain()

### Create the players
alien = Alien("Geoff")
marine = Marine("Steve",5)

### Go!
runGame()
