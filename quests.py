class Quest:
    def __init__(self, title, description, reward):
        self.title = title
        self.description = description
        self.reward = reward
        self.completed = False

    def complete(self):
        self.completed = True
        return self.reward

# Example usage:
# quest = Quest('Find the Lost Sword', 'Retrieve the sword from the goblin cave.', '100 gold')
# reward = quest.complete()  # Completes the quest and gives reward