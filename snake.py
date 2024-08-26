import keyboard
import os
import time
import random

# Global variables

logo = """
   _____             _        
  / ____|           | |       
 | (___  _ __   __ _| | _____ 
  \___ \| '_ \ / _` | |/ / _ \\
  ____) | | | | (_| |   <  __/
 |_____/|_| |_|\__,_|_|\_\___|
                                                        
"""

x_max, y_max = 50, 25
x, y = 25, 12
length = 10
direction = "down"
clear_command = "cls" if os.name == "nt" else "clear"
runner_char = "█"
background_char = "░"
food_char = "@"
snake_body = [(x, y)]  # Initial position of the snake's head
opposite_directions = {"up": "down", "down": "up", "left": "right", "right": "left"}
display = []
food_count = 30
score = 0 
max_score = food_count

def change_direction(new_direction):
    global direction
    if new_direction != opposite_directions[direction]:
        direction = new_direction

def move_snake():
    global x, y, snake_body, score

    while True:
        os.system(clear_command)

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

        if display[y][x] == food_char:
            score += 1

        # Remove the last part of the snake's tail if the snake exceeds its length
        if len(snake_body) > length:
            tail_x, tail_y = snake_body.pop()
            display[tail_y][tail_x] = background_char  # Clear the last position

        if score == max_score:
            break

        # Update the display with the snake's current position
        for segment in snake_body:
            display[segment[1]][segment[0]] = runner_char

        print("\n".join("".join(line) for line in display))
        print(f"Score: {score}")
        time.sleep(0.1)

def splash():
    os.system(clear_command)
    print(logo)
    print("Loading...")
    time.sleep(4)

def main():
    global display, food_count
    display = [[background_char for _ in range(x_max)] for _ in range(y_max)]

    while food_count > 0:
        x_val = random.randint(0, x_max - 1)
        y_val = random.randint(0, y_max - 1)

        if display[y_val][x_val] != food_char:
            display[y_val][x_val] = food_char
            food_count -= 1

    keyboard.add_hotkey('8', change_direction, args=("up",))
    keyboard.add_hotkey('4', change_direction, args=("left",))
    keyboard.add_hotkey('2', change_direction, args=("down",))
    keyboard.add_hotkey('6', change_direction, args=("right",))

if __name__ == "__main__":
    try:
        splash()
        main()
        move_snake()
    except KeyboardInterrupt:
        print("Exit")