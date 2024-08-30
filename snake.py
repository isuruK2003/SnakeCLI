import keyboard
import os
import time
import random

# Global variables

logo = """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║                                                            ║
║   ________  ________   ________  ___  __    _______        ║
║  |\   ____\|\   ___  \|\   __  \|\  \|\  \ |\  ___ \       ║
║  \ \  \___|\ \  \\\\ \  \ \  \|\  \ \  \/  /|\ \   __/|      ║
║   \ \_____  \ \  \\\\ \  \ \   __  \ \   ___  \ \  \_|/__    ║
║    \|____|\  \ \  \\\\ \  \ \  \ \  \ \  \\\\ \  \ \  \_|\ \   ║
║      ____\_\  \ \__\\\\ \__\ \__\ \__\ \__\\\\ \__\ \_______\  ║
║     |\_________\|__| \|__|\|__|\|__|\|__| \|__|\|_______|  ║
║     \|_________|                                           ║
║                                                            ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
"""

x_max = 50
y_max = 25
x = int(x_max / 2)
y = int(y_max / 2)
length = int(y_max / 2)
clear_command = "cls" if os.name == "nt" else "clear"
runner_char = "█"
background_char = "░"
food_char = "@"
snake_body = [(x, y)]  # Initial position of the snake's head
directions = {"up": "down", "down": "up", "left": "right", "right": "left"}
direction = random.choice(list(directions.keys()))
display = []
score = 0

def change_direction(new_direction):
    global direction
    if new_direction != directions[direction]:
        direction = new_direction

def place_food():
    global food_count, display

    x_val = random.randint(0, x_max - 1)
    y_val = random.randint(0, y_max - 1)

    if (x_val, y_val) in snake_body:
        place_food()

    display[y_val][x_val] = food_char

def move_snake():
    global x, y, snake_body, score, display, length

    while True:
        dx, dy = 0, 0
        if direction == "up":
            dy = -1
        elif direction == "down":
            dy = 1
        elif direction == "right":
            dx = 1
        elif direction == "left":
            dx = -1
        
        # Calculate new head position
        x = (x + dx) % x_max
        y = (y + dy) % y_max

        # Insert new head position at the front of the snake body
        snake_body.insert(0, (x, y))

        # snake eat food, length of the snake is increased by one unit4
        # score increased by one and new food is placed
        if display[y][x] == food_char:
            score += 1
            length += 1
            place_food()

        # If snake hits itself, end the game
        if display[y][x] == runner_char:
            break

        # Remove the last part of the snake's tail if the snake exceeds its length
        if len(snake_body) > length:
            tail_x, tail_y = snake_body.pop()
            display[tail_y][tail_x] = background_char  # Clear the last position

        # Update the display with the snake's current position
        for segment in snake_body:
            display[segment[1]][segment[0]] = runner_char

        os.system(clear_command)
        print("\n".join("".join(line) for line in display))
        print(f"Score: {score}")
        time.sleep(0.05)

def splash():
    os.system(clear_command)
    print(logo)
    time.sleep(2)

def main():
    global display, food_count
    display = [[background_char for _ in range(x_max)] for _ in range(y_max)]

    place_food()

    keyboard.add_hotkey('8', change_direction, args=("up",))
    keyboard.add_hotkey('4', change_direction, args=("left",))
    keyboard.add_hotkey('2', change_direction, args=("down",))
    keyboard.add_hotkey('6', change_direction, args=("right",))

if __name__ == "__main__":
    try:
        splash()
        main()
        move_snake()
        print("Game Over!")
    except KeyboardInterrupt:
        print("Exit")
