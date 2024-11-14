# Sudoku Solver Bot

### Description
**Sudoku Solver Bot** is a Python program that automatically solves sudoku puzzles on [sudoku.com](https://sudoku.com/). The bot performs the following steps:
1. Takes a screenshot of the sudoku grid from the screen.
2. Uses a neural network to recognize the digits in the grid.
3. Solves the sudoku puzzle.
4. Automatically fills in the correct digits on the website using simulated mouse clicks.
5. Proceeds to the next sudoku puzzle on the website and repeats the process.

### Technologies and Libraries
The project utilizes the following libraries:
- `TensorFlow` — for a pretrained model (MNIST) to recognize digits.
- `OpenCV` — for image processing and sudoku grid preprocessing.
- `pyautogui` — for simulating mouse actions and screen interactions.
- `keyboard` — for controlling the start and stop of the program.

### Project Structure
The project is organized as follows:
```bash
sudoku_solver_bot/
├── data/                          # Folder with data
│   └── sudoku.png                 # Example sudoku image for testing
├── models/                        # Folder with the recognition model
│   └── model.h5                   # Model trained on MNIST for digit recognition
├── src/                           # Source code
│   ├── sudoku_interaction.py      # Module for website interaction (using pyautogui)
│   ├── sudoku_recognize.py        # Module for digit recognition in the screenshot
│   ├── sudoku_solve.py            # Module for solving sudoku
│   └── __init__.py
├── main.py                        # Main file to run the program
├── requirements.txt               # List of dependencies
└── README.md                      # Project documentation
```


### Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/smgbaid/sudoku_solver_bot.git
    cd sudoku_solver_bot
    ```

2. **Install dependencies**:
    Ensure that you have Python 3.12 or higher installed. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Coordinate adjustment**:
    The program takes a screenshot of the sudoku grid based on screen coordinates. You may need to adjust the coordinates in the code according to your screen resolution and browser settings.

### Usage

1. **Navigate to** [sudoku.com](https://sudoku.com/) and open a sudoku game.
2. **Run the program**:
    ```bash
    python main.py
    ```
3. Ensure that the sudoku grid is visible on the screen and press the `s` key to start the program loop.
4. The program will take a screenshot of the sudoku, recognize the digits, solve the puzzle, and fill in the solution on the website. After completing the sudoku, it will automatically move to the next puzzle and repeat the process.

> **Note**: If you need to stop the program, press the `Esc` key.

### Example Image

An example sudoku image for testing is located at `data/sudoku.png`.

### Environment Requirements
- Python version 3.12 or higher.
- Running `pyautogui` and `keyboard` libraries requires administrator privileges (in Windows) or `sudo` (on macOS/Linux) for proper functionality.
