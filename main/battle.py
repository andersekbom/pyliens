from random import randint
from time import sleep

def doBattle(territory, attackers):

    print
    print "Rolling the dice..."
    sleep(1)

    attackerDice = []
    defenderDice = []
    
    ## Roll the dice for each side ##
    for dice in range(0,attackers):
        attackerDice.append(randint(1,6))
    for dice in range(0,territory.troops):
        defenderDice.append(randint(1,6))

    ## Sort the results ##
    attackerDice.sort(reverse=True)
    defenderDice.sort(reverse=True)

    ## Find out if we're comparing 1 or 2 die.
    ## If only 1 attacker or defender then only 1 fight
    if len(attackerDice) == 1 or len(defenderDice) == 1: 
        fights = 1
    else:
        fights = 2
    
    attackerLost = 0
    defenderLost = 0
    
    ## Fight! ##
    for i in range(0,fights):
        #print "%s vs %s" % (attackerDice[i],defenderDice[i])
        if cmp(attackerDice[i],defenderDice[i]) <1:
            attackerLost +=1
        else:
            defenderLost +=1
            
    return (defenderLost,attackerLost)

