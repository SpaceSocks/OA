class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class Quest:
    def __init__(self, title, description, reward):
        self.title = title
        self.description = description
        self.reward = reward

# Example usage:
# sword = Item('Sword', 'A sharp blade.')
# goblin = Enemy('Goblin', 30, 5)
# quest = Quest('Save the Village', 'Defeat the goblin menace.', '100 gold')