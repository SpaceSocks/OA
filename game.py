import sys
import os
import msvcrt
import pygame
from ansi_graphics import ANSI
from game_mechanics import Item, Enemy, Quest

class Game:
    def __init__(self):
        self.map = self.create_map()
        self.player_position = (1, 1)
        self.inventory = []
        self.enemies = [Enemy('Goblin', 30, 5)]
        self.quests = [Quest('Find the Lost Sword', 'Retrieve the sword from the goblin cave.', '100 gold')]
        pygame.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def create_map(self):
        return [
            ['.', '.', '.', 'X'],
            ['.', 'P', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', 'X', '.']
        ]

    def display_map(self):
        ANSI.clear_screen()
        for row in self.map:
            for cell in row:
                if cell == 'P':
                    ANSI.set_color(32, 40)  # Green text on black background
                else:
                    ANSI.set_color(37, 40)  # White text on black background
                print(cell, end=' ')
            ANSI.reset()
            print()  # New line after each row

    def move_player(self, direction):
        x, y = self.player_position
        if direction == 'up' and x > 0:
            self.player_position = (x - 1, y)
        elif direction == 'down' and x < len(self.map) - 1:
            self.player_position = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.player_position = (x, y - 1)
        elif direction == 'right' and y < len(self.map[0]) - 1:
            self.player_position = (x, y + 1)
        self.update_map()

    def update_map(self):
        self.map = [['.' for _ in range(len(self.map[0]))] for _ in range(len(self.map))]
        x, y = self.player_position
        self.map[x][y] = 'P'

    def run(self):
        while True:
            self.display_map()
            command = self.get_input()
            if command in ['up', 'down', 'left', 'right']:
                self.move_player(command)
            elif command == 'quit':
                break
            elif command == 'inventory':
                self.show_inventory()
            elif command == 'attack':
                self.attack_enemy()
            elif command == 'quests':
                self.show_quests()
            elif command.startswith('complete '):
                quest_title = command.split(' ', 1)[1]
                self.complete_quest(quest_title)

    def show_inventory(self):
        if not self.inventory:
            print('Inventory is empty.')
        else:
            print('Inventory:')
            for item in self.inventory:
                print(f'- {item.name}: {item.description}')

    def attack_enemy(self):
        if self.enemies:
            enemy = self.enemies[0]  # Attack the first enemy
            print(f'Attacking {enemy.name}!')
            enemy.take_damage(10)  # Example damage
            if enemy.health <= 0:
                print(f'{enemy.name} defeated!')
                self.enemies.remove(enemy)
        else:
            print('No enemies to attack.')

    def show_quests(self):
        if not self.quests:
            print('No quests available.')
        else:
            print('Available Quests:')
            for quest in self.quests:
                status = 'Completed' if quest.completed else 'In Progress'
                print(f'- {quest.title}: {status}')

    def complete_quest(self, title):
        for quest in self.quests:
            if quest.title.lower() == title.lower() and not quest.completed:
                reward = quest.complete()
                print(f'Quest completed! You received: {reward}')
                return
        print('Quest not found or already completed.')

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # A button
                    return 'up'
                elif event.button == 1:  # B button
                    return 'down'
                elif event.button == 2:  # X button
                    return 'left'
                elif event.button == 3:  # Y button
                    return 'right'
        return input('Enter command (up, down, left, right, quit, inventory, attack, quests, complete <quest title>): ').strip().lower()

if __name__ == '__main__':
    game = Game()
    game.run()