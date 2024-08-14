import sys
import os

class Game:
    def __init__(self):
        self.map = self.create_map()
        self.player_position = (0, 0)

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
            command = input('Enter command (up, down, left, right, quit): ').strip().lower()
            if command in ['up', 'down', 'left', 'right']:
                self.move_player(command)
            elif command == 'quit':
                break

if __name__ == '__main__':
    game = Game()
    game.run()