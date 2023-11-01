import pygame

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
# # #


# Shop functions
def store_call():
    for item_type in shop.keys():
        print(f"\n{item_type}:") 
        for key in shop[item_type].keys():
            print(f"\t{key}: {shop[item_type][key]['name']} ({shop[item_type][key]['price']})")


def buy(player_max_health, player_damage, crit_chance, player_health, player_money, player_max_health_base, player_damage_base, shop, player_input, player_mana, player_max_mana):
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
def win(enemy, player, enemy_counter, sound):
    pygame.mixer.Sound.play(sound)
    return player.money+enemy.reward, enemy_counter+1

def lose_check(player_health):
    """Returns True if the player's health reaches 0"""
    if player_health <= 0:
        return True
    return False