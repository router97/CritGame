""" Welcome! """

import random
import time
from enemy import *
from shop import *

enemy_counter = 1
def Intro():
    global enemy_counter
    print(" * Type (a) to ⚔-ATTACK-⚔")
    print(" * Type (s) to open the [-STORE-] and (buy 'name of the product') to BUY it")
    print(' * Type (buy "name of the product") to $-BUY-$ it')
    # print("\n\t\t --- Enemy - {0} ---".format(enemies[enemy_counter]["name"]))
    # print("\t\t{0}(ATK = {1}, HP = {2})".format(enemies[enemy_counter]["name"], 
    #                                     enemies[enemy_counter]["damage"], 
    #                                     enemies[enemy_counter]["health"]))
Intro()


""" setting values for variables """
EnemyHealth = enemies[enemy_counter]["health"]
EnemyDamage = enemies[enemy_counter]["damage"]
PlayerHealth = 100
PlayerMaxHealth = 100
PlayerMana = 100
PlayerMaxMana = 100
PlayerDamage = 99
CritChance = 4
enemy_counter = 1
PlayerMoney = 0


""" functions (attacks, healing etc.) """
def Attack():
    global EnemyHealth
    print(" * Hit")
    EnemyHealth = EnemyHealth - PlayerDamage

def CritAttack():
    global EnemyHealth
    print(" * CRITICAL HIT!")
    EnemyHealth = EnemyHealth - (PlayerDamage * 2)

def Heal(mana = False, PlayerHealAmountMana = 0, PlayerHealAmount = 0):
    global PlayerHealth, PlayerMaxHealth, PlayerMana, PlayerMaxMana
    print(" * Healing...")
    if mana == True:
        if PlayerMana == PlayerMaxMana:
            print(" * Full mana")
        elif PlayerMana >= PlayerMaxMana - PlayerHealAmountMana:
            PlayerMana = PlayerMaxMana
        else:
            PlayerMana = PlayerMana + PlayerHealAmountMana
        return None
    if PlayerHealth == PlayerMaxHealth:
        print(" * Full health")
    elif PlayerHealth >= PlayerMaxHealth - PlayerHealAmount:
        PlayerHealth = PlayerMaxHealth
    else:
        PlayerHealth = PlayerHealth + PlayerHealAmount

def WinCheck():
    global EnemyHealth, enemy_counter, EnemyDamage, PlayerMoney
    if EnemyHealth <= 0:
        
        print(" --- You win! ---")
        try:
            PlayerMoney = PlayerMoney + enemies[enemy_counter]["reward"]
            enemy_counter = enemy_counter + 1
            EnemyHealth = enemies[enemy_counter]["health"]
            EnemyDamage = enemies[enemy_counter]["damage"]
            Intro()
        except KeyError:
            exit()

def LoseCheck():
    global PlayerHealth
    if PlayerHealth <= 0:
        print("--- You lose! ---")
        exit()

def CounterAttack():
    global PlayerHealth
    print(" * COUNTER ATTACK!")
    PlayerHealth = PlayerHealth - EnemyDamage

def StoreCall():
    for itemType in shop.keys():
        print("\n" + itemType + ":") 
        for key in shop[itemType].keys():
            print("\t{1}: {2} ({3})".format(itemType, key, shop[itemType][key]["name"], shop[itemType][key]["price"]))

def Buy():
    global PlayerMaxHealth, PlayerDamage, CritChance, PlayerHealth, PlayerMoney
    item = PlayerInput.strip("buy").strip(" ").lower()
    for itemType in shop.keys():
        for key in shop[itemType].keys():
            if shop[itemType][key]["name"] == item:
                if itemType == "equipment":
                    if PlayerMoney >= shop[itemType][key]["price"]:
                        print(" * bought", item)
                        try:
                            PlayerMaxHealth = shop[itemType][key]["health"]
                            PlayerHealth = PlayerMaxHealth
                        except KeyError:
                            PlayerDamage = shop[itemType][key]["damage"]
                            CritChance = shop[itemType][key]["crit"]
                if itemType == "consumables":
                    if item == "health potion":
                        print(" * bought", item)
                        Heal(False, None, shop[itemType][key]["heal"])
                    if item == "mana potion":
                        print(" * bought", item)
                        Heal(True, shop[itemType][key]["mana"])
            if PlayerMoney >= shop[itemType][key]["price"]:
                PlayerMoney = PlayerMoney - shop[itemType][key]["price"]


""" user input loop """
while True:
    print("\n\t\t --- Enemy - {0} ---".format(enemies[enemy_counter]["name"]))
    print("\t\t  (ATK = {0}, HP = {1})".format( 
                                        enemies[enemy_counter]["damage"], 
                                        enemies[enemy_counter]["health"]))
    print("\n\t\t      --- You --- \n\t     (HP = {0}, MANA = {1}, MONEY = {2})\n"
                                                                .format(PlayerHealth, PlayerMana, PlayerMoney))
    PlayerInput = input("-> ")
    RandomInt = (random.randint(0, 10))
    if PlayerInput == "a":
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
    elif PlayerInput == "s":
        StoreCall()
        PlayerInput = ("")
    elif PlayerInput[0:3] == "buy":
        Buy()
        if RandomInt >= 8:
            RandomInt = (random.randint(0, 10))
            if RandomInt >= 8:
                time.sleep(0.5)
                CounterAttack()
                LoseCheck()
        PlayerInput = ("")
    else:
        if RandomInt >= 8:
            time.sleep(0.5)
            CounterAttack()
            LoseCheck()
        PlayerInput = ("")