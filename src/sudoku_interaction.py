import os
import sys
import time
import random
import keyboard
import pyautogui

def get_sudoku_image():
    x, y, w, h = 99, 307, 690, 690
    image_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'sudoku.png'))
    pyautogui.screenshot(image_dir, region=(x, y, w, h))

def fill_sudoku(sudoku_grid):
    start_x, start_y = 137, 333
    cell_size = 76
    for row in range(9):
        for col in range(9):
            if sudoku_grid[row][col] != 0:
                if keyboard.is_pressed('esc'):
                    print("Program stop")
                    sys.exit()
                else:
                    x = start_x + col * cell_size
                    y = start_y + row * cell_size

                    pyautogui.click(x, y)
                    pyautogui.typewrite(str(sudoku_grid[row][col]))
                    time.sleep(random.uniform(0.1, 1.0))

def next_sudoku():
    coordinates = {
        "medium": (850, 500),
        "hard": (850, 550),
        "expert": (850, 620),
        "master": (850, 690),
    }
    # Press "Next game"
    pyautogui.click(850, 950)
    time.sleep(0.5)
    # Choose a difficulty level
    random_key = random.choice(list(coordinates.keys()))
    random_coords = coordinates[random_key]
    pyautogui.click(random_coords)
    time.sleep(5)
