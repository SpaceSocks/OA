class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f'{self.name} has been defeated!')

# Example usage:
# goblin = Enemy('Goblin', 30, 5)
# goblin.take_damage(10)  # Goblin takes 10 damage