import json

class Enemy:
    def __init__(self, name, health, damage, reward):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.reward = reward
    
    def __str__(self):
        return f"{self.name}|{self.health}|{self.damage}|{self.reward}"
    
    @staticmethod
    def create_from_json(fl):
        """Takes a json string of enemies, turns it into a list of enemies.

        Args:
            fl (str): json file.

        Returns:
            list: list of enemy objects.
        """
        enemies = [] # Create a hollow list.
        json_load = json.load(fl) # Load JSON file into a dictionary.
        for key, value in json_load.items(): # Go through each enemy.
            name = value['name'] 
            health = value['health']
            damage = value['damage']
            reward = value['reward']
            enemy = Enemy(name, health, damage, reward) # Create an Enemy class object with stats from JSON.
            enemies.append(enemy) # Append the Enemy class object to a list.
        return enemies 




class EnemyBoss(Enemy):
    """A different kind of enemy, with a theme.

    Args:
        Enemy (class): The original Enemy class.
    """
    
    def __init__(self, name, health, damage, reward, theme):
        super().__init__(name, health, damage, reward)
        self.theme = theme

    def __str__(self):
        return f"{self.name}|{self.health}|{self.damage}|{self.reward}|{self.theme}"