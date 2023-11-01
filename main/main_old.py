""" Welcome! """

import random
import time
import json
with open("main/data/enemy.json", "r") as fl:
    # Load the JSON data into a dictionary
    json_enemies = json.load(fl)
with open("main/data/shop.json", "r") as fl:
    # Load the JSON data into a dictionary
    json_shop = json.load(fl)

enemies = {int(key): value for key, value in json_enemies.items()} # Converting enemy index into an integer
shop = {
    item_type: {
        int(key): value
        for key, value in items.items()
    }
    for item_type, items in json_shop.items()
} # Converting shop index into an integer


enemy_counter = 1
def Intro():
    print(" * Type (a) to ⚔-ATTACK-⚔")
    print(" * Type (s) to open the [-STORE-] and (buy 'name of the product') to BUY it")
    print(' * Type (buy "name of the product") to $-BUY-$ it')
Intro()

def round_print(enemy_counter, player_health, player_mana, player_money, enemy_damage, enemy_health, enemies, player_damage):
    print("\n\t\t --- Enemy - {0} ---".format(enemies[enemy_counter]["name"]))
    print("\t\t  (ATK = {0}, HP = {1})".format(enemy_damage, enemy_health))
    print("\n\t\t      --- You --- \n\t(HP = {0}, MANA = {1}, MONEY = {2}, DMG = {3})\n".format(player_health, player_mana, player_money, player_damage))

# Initialising variables
enemy_health = enemies[enemy_counter]["health"]
enemy_damage = enemies[enemy_counter]["damage"]
player_health = 100
player_max_health = 100
player_max_health_base = 100
player_mana = 100
player_max_mana = 100
player_max_mana_base = 100
player_damage = 99
player_damage_base = 99
crit_chance = 4
enemy_counter = 1
player_money = 100
player_input = ''

player_stats = (
    
    player_health,
    player_max_health,
    player_max_health_base,
    
    player_mana,
    player_max_mana,
    player_max_mana_base,
    
    player_damage,
    player_damage_base,
    crit_chance,
    
    player_money)

# Functions to handle attacks
def attack(enemy_health, player_damage):
    """Reduces the enemy's health by the player's damage."""
    return enemy_health - player_damage

def crit_attack(enemy_health, player_damage):
    """Performs a critical attack on the enemy, reducing its health by twice the player's damage."""
    return enemy_health - player_damage * 2

def counter_attack(player_health, enemy_damage):
    """Resolves an enemy's counter-attack, reducing the player's health by the enemy's damage."""
    return player_health - enemy_damage

# Healing
def heal(player_stat, player_max_stat, amount):
    if player_stat == player_max_stat:
        pass
    elif player_stat >= player_max_stat-amount:
        player_stat = player_max_stat
    else:
        player_stat += amount
    return player_stat, player_max_stat

# Shop functions
def store_call():
    for item_type in shop.keys():
        print(f"\n{item_type}:") 
        for key in shop[item_type].keys():
            print(f"\t{key}: {shop[item_type][key]['name']} ({shop[item_type][key]['price']})")

def buy(player_max_health, player_damage, crit_chance, player_health, player_money, player_max_health_base, player_damage_base):
    no_money = False
    item = player_input.strip("buy").strip().lower() # Getting the item name
    
    for item_type in shop.keys(): # Searching through item types
        if no_money: # If the player doesn't have enough money for the item
            break # Break out of the types loop
        print('TYPEEEEEE')
        for key in shop[item_type].keys(): # Searching through items
            print('item')
            item_key = shop[item_type][key] # Lessen the adress
                
            if item_key["name"] == item: # If the item name matches the input
                if player_money < item_key["price"]: # If player doesn't have enough money
                    no_money = True # Setting no_money to True
                    break # Breaking out of items loop
                player_money -= item_key['price'] # Reducing player money by item price
                
                print(" * bought", item)
                if item_type == "equipment":
                    
                    if player_money >= item_key["price"]:
                        
                        player_max_health_get = item_key.get("health")
                        player_damage_get = item_key.get("damage")
                        crit_chance_get = item_key.get("crit")
                        player_max_health = player_max_health_base
                        player_damage = player_damage_base
                        
                        if player_max_health_get is not None:
                            player_max_health += item_key['health']
                            player_health = player_max_health
                        
                        if player_damage_get is not None:
                            player_damage += item_key['damage']
                        
                        if crit_chance_get is not None:
                            crit_chance = item_key['crit']
                
                elif item_type == "consumables":
                    if item_key['type'] == 'health':
                        stats = (player_health, player_max_health)
                    if item_key['type'] == 'mana':
                        stats = (player_mana, player_max_mana)
                    player_stat, player_max_stat = stats
                    stats = heal(player_stat, player_max_stat, item_key['heal'])  
            
                else:
                    continue 
    updated_stats = (player_health, player_max_health, player_mana, player_max_mana,
                     player_damage, crit_chance, player_money)
    return updated_stats

# Functions to handle round progression
def win(enemy_counter, enemy_health, enemy_damage, player_money, enemies):
    """Updates enemy stats with the next enemy's stats, if current enemy's health reaches 0 and it isn't the last enemy"""
    enemy_stats = enemies[enemy_counter]
    enemy_counter += 1
    enemy_health, enemy_damage, reward = enemy_stats["health"], enemy_stats["damage"], enemy_stats["reward"]
    player_money += reward
    return enemy_counter, enemy_health, enemy_damage, player_money

def lose_check(player_health):
    """Returns True if the player's health reaches 0"""
    if player_health <= 0:
        return True
    return False


# Main game loop
playing = True
while playing:
    round_print(enemy_counter, player_health, player_mana, player_money, enemy_damage, enemy_health, enemies, player_damage)
    player_input = input("-> ")
    random_int = (random.randint(0, 10))
    time.sleep(0.5)
    
    # Attacks
    if player_input == 'a':
        if random_int <= crit_chance:
            print(" * Hit")
            enemy_health = attack(enemy_health, player_damage)
        elif random_int in (5, 6, 7):
            print(" * CRITICAL HIT!")
            enemy_health = crit_attack(enemy_health, player_damage)
    
    # Shop
    elif player_input == 's':
        store_call()
    
    elif player_input[0:3] == 'buy':
        new_values = (buy(player_max_health, player_damage, crit_chance, player_health, player_money, player_max_health_base, player_damage_base))
        player_health, player_max_health, player_mana, player_max_mana, player_damage, crit_chance, player_money = new_values
    
    # Counter attack
    if random_int >= 8 and player_input is not 's':
        print(" * COUNTER ATTACK!")
        player_health = counter_attack(player_health,enemy_damage)
    
    # Round progression
    if lose_check(player_health):
        print("--- You lose! ---")
        playing = False
    elif enemy_health <= 0:
        print(" --- You win! ---")
        enemy_counter, enemy_health, enemy_damage, player_money = win(enemy_counter, enemy_health, enemy_damage, player_money, enemies)
        if enemy_counter > len(enemies):
            playing = False