# # # game starts # # #
import random
import time
from enemy import *
from shop import *
print(" * Started!")
print(" * Type (attack) to attack, (heal) to heal")
print(" * Type (store) to open the store and (buy 'name of the product') to buy it")
print(" --- Enemy - {0} ---".format(enemies[1]["name"]))
print("{0}(ATK = {1}, HP = {2})".format(enemies[1]["name"], 
                                        enemies[1]["damage"], 
                                        enemies[1]["health"]))


# # # setting values for variables # # #
EnemyHealth = enemies[1]["health"]
EnemyDamage = enemies[1]["damage"]
PlayerHealth = 100
PlayerMaxHealth = 100
PlayerDamage = 100
HealAmount = 20
CritChance = 4
enemy_counter = 1

# # # functions (attacks, healing etc.) # # #
def Attack():
    global EnemyHealth
    print("Hit")
    EnemyHealth = EnemyHealth - PlayerDamage
    print("Enemy =", EnemyHealth)

def CritAttack():
    global EnemyHealth
    print("CRITICAL HIT!")
    EnemyHealth = EnemyHealth - (PlayerDamage * 2)
    print("Enemy =", EnemyHealth)

def Heal():
    global PlayerHealth
    print("Healing...")
    if PlayerHealth == PlayerMaxHealth:
        print("Full health")
    elif PlayerHealth >= PlayerMaxHealth - HealAmount:
        PlayerHealth = PlayerMaxHealth
    else:
        PlayerHealth = PlayerHealth + HealAmount
    print("You =", PlayerHealth)

def WinCheck():
    global EnemyHealth
    global enemy_counter
    global EnemyDamage
    if EnemyHealth <= 0:
        
        print(" --- You win! ---")
        try:
            enemy_counter = enemy_counter + 1
            EnemyHealth = enemies[enemy_counter]["health"]
            EnemyDamage = enemies[enemy_counter]["damage"]
            print(" * Type (attack) to attack, (heal) to heal")
            print(" * Type (store) to open the store and (buy 'name of the product') to buy it")
            print(" --- Enemy - {0} ---".format(enemies[enemy_counter]["name"]))
            print("{0}(ATK = {1}, HP = {2})".format(enemies[enemy_counter]["name"], 
                                                     enemies[enemy_counter]["damage"], 
                                                     enemies[enemy_counter]["health"]))
        except KeyError:
            exit()
            

def LoseCheck():
    global PlayerHealth
    if PlayerHealth <= 0:
        print("--- You lose! ---")
        exit()

def CounterAttack():
    global PlayerHealth
    print("COUNTER ATTACK!")
    PlayerHealth = PlayerHealth - EnemyDamage
    print("You =", PlayerHealth)

def StoreCall():
    for key in store.keys():
        print("item {0}: {1}\n{2}".format(key, store[key]["name"], store[key]))

def Buy():
    global PlayerMaxHealth, HealAmount, PlayerDamage, CritChance
    for i in PlayerInput[2:]:
        if i.isspace()== False:
            item = item+i
    item = int(PlayerInput[2:])
    print(item)
    if store[item]["health"] != None:
        PlayerMaxHealth = store[item]["health"]
    if store[item]["heal"] != None:
        HealAmount = store[item]["heal"]
    if store[item]["damage"] != None:
        PlayerDamage = store[item]["damage"]
    if store[item]["crit"] != None:
        CritChance = store[item]["crit"]

# # # user input loop # # #
while 1 == 1:
    PlayerInput = input("")
    RandomInt = (random.randint(0, 10))
    if PlayerInput == "attack":
        if RandomInt <= CritChance:
            time.sleep(0.5)
            Attack()
            WinCheck()
            PlayerInput = ("")
        elif RandomInt == 5 or RandomInt == 6 or RandomInt == 7 :
            time.sleep(0.5)
            CritAttack()
            WinCheck()
            PlayerInput = ("")
        else:
            time.sleep(0.5)
            CounterAttack()
            LoseCheck()
            PlayerInput = ("")
    elif PlayerInput == "heal":
        if RandomInt >= 8:
            RandomInt = (random.randint(0, 10))
            if RandomInt >= 8:
                time.sleep(0.5)
                CounterAttack()
                LoseCheck()
        time.sleep(0.5)
        Heal()
        LoseCheck()
        WinCheck()
        PlayerInput = ("")
    elif PlayerInput == "store":
        StoreCall()
    # elif:
    #     print("jern")
    #     Buy()
    else:
        if RandomInt >= 8:
            time.sleep(0.5)
            CounterAttack()
            LoseCheck()
        PlayerInput = ("")