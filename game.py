import sys
import os
import msvcrt
import pygame

class Game:
    def __init__(self):
        self.map = self.create_map()
        self.player_position = (1, 1)
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
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.map:
            print(' '.join(row))

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
        return input('Enter command (up, down, left, right, quit): ').strip().lower()

if __name__ == '__main__':
    game = Game()
    game.run()