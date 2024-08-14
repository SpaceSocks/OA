class ANSI:
    @staticmethod
    def clear_screen():
        print('\033[H\033[J')  # Clear screen

    @staticmethod
    def set_color(fg, bg):
        print(f'\033[{fg};{bg}m', end='')

    @staticmethod
    def reset():
        print('\033[0m', end='')

# Example usage:
# ANSI.clear_screen()
# ANSI.set_color(31, 40)  # Red text on black background
# print('Hello, World!')
# ANSI.reset()