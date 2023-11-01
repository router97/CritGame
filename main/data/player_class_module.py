class Player:
    
    action = None
    
    def __init__(self, health, damage, crit_chance, money):
        self.health = health
        self.max_health = health
        self.damage = damage
        self.crit_chance = crit_chance
        self.money = money
    
    def __str__(self):
        return f"{self.health}|{self.damage}|{self.crit_chance}|{self.money}"
    
    def heal(self, amount):
        """Heals the player by the amount given, not reaching over the max health.

        Args:
            amount (int): Heal amount.
        """
        if self.health == self.max_health:
            return
        elif self.health >= self.max_health-amount:
            self.health = self.max_health
        else:
            self.health += amount