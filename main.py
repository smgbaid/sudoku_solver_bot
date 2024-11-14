from src.sudoku_recognize import load_model, prepare_image, process_sudoku_grid
from src.sudoku_interaction import get_sudoku_image, fill_sudoku, next_sudoku
from src.sudoku_solve import solve_sudoku
import os
import copy
import time
import keyboard

def sudoku_negative(sudoku_grid, old_sudoku_grid):
    for row in range(9):
        for col in range(9):
            if sudoku_grid[row][col] == old_sudoku_grid[row][col]:
                sudoku_grid[row][col] = 0

def main():
    os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
    model_path = os.path.join("models", "model.h5")
    model = load_model(model_path)

    while True:
        get_sudoku_image()
        image_path = os.path.join("data", "sudoku.png")
        # Preprocess image and sudoku recognition
        image = prepare_image(image_path)

        sudoku_grid = process_sudoku_grid(image, model)
        old_sudoku_grid = copy.deepcopy(sudoku_grid)
        print("Sudoku grid")
        for row in sudoku_grid:
            print(row)

        if solve_sudoku(sudoku_grid):
            print("Sudoku solution:")
            for row in sudoku_grid:
                print(row)

            sudoku_negative(sudoku_grid, old_sudoku_grid)
            fill_sudoku(sudoku_grid)
            print("SUDOKU SOLVED !!")
            time.sleep(3)
            next_sudoku()
        else:
            print("Sudoku has no solutions")
            next_sudoku()

        if keyboard.is_pressed('esc'):
            break

if __name__ == '__main__':
    keyboard.add_hotkey('s', main)
    print("Program is running!")
    keyboard.wait('esc')
