import json
import os


# Enemies
path = "main/data/enemy.json"
json_dict = {
    1: {
    "name": "Zevaka",
    "health": 1,
    "damage": 1,
    "reward": 1
    }
    ,
    2: {
    "name": "Gleb",
    "health": 1,
    "damage": 1,
    "reward": 1
    }
    ,
    3: {
    "name": "MAKAROV",
    "health": 1,
    "damage": 1,
    "reward": 1
    }
}
with open(path, "w") as fl:
    fl.write(json.dumps(json_dict, indent=4))


# Shop items
path = "main/data/shop.json"
json_dict = {
    "equipment":{
        1: {
            "name": "sword",
            "price": 100,
            "damage": 9999,
            "crit": 7
        },
        2: {
            "name": "armor",
            "price": 150,
            "health": 250
    }
    },    
        
    "consumables":{
        1: {
            "name": "health potion",
            "price": 50,
            "heal": 50
        },
        2: {
            "name": "mana potion",
            "price": 50,
            "mana": 50
        }
    }
}
with open(path, "w") as fl:
    fl.write(json.dumps(json_dict, indent=4))