import pygame

class Controller:
    def __init__(self):
        pygame.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

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
        return None

# Example usage:
# controller = Controller()
# while True:
#     command = controller.get_input()
#     if command:
#         print(f'Controller command: {command}')