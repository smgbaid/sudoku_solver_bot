import tensorflow as tf
import numpy as np
import cv2

def view_image(image, name_of_window: str):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def is_digit_exist(predictions, threshold=0.3):
    predicted_class = np.argmax(predictions)
    confidence = predictions[0][predicted_class]
    if confidence > threshold:
        return True
    return False

def is_not_one(predictions):
    predicted_class = np.argmax(predictions)
    if predicted_class in [1, 7]:
        diff_7 = abs(predictions[0][7] - predictions[0][1])
        if diff_7 < 0.96:
            return False
    if predicted_class in [1, 9]:
        diff_9 = abs(predictions[0][9] - predictions[0][1])
        if diff_9 < 0.8:
            return False
    return True

def prepare_image(image_path, debug=False):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Image not found.")
        return
    thresh_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    if debug:
        view_image(thresh_image, 'Thresholded Image')
    return thresh_image

def process_cell(cell, model, debug=False):
    cell = cv2.resize(cell, (28, 28))
    cell = cell / 255.0
    cell = cell.reshape(1, 28, 28, 1)
    predictions = model.predict(cell)
    predicted_digit = np.argmax(predictions)

    if is_digit_exist(predictions):
        if is_not_one(predictions):
            return int(predicted_digit)
        else:
            return 1
    return 0

def process_sudoku_grid(thresh_image, model, debug=False):
    cell_height = thresh_image.shape[0] // 9
    cell_width = thresh_image.shape[1] // 9
    sudoku_grid = []

    for row in range(9):
        row_list = []
        for col in range(9):
            y1, y2 = row * cell_height, (row + 1) * cell_height
            x1, x2 = col * cell_width, (col + 1) * cell_width
            cell = thresh_image[y1:y2, x1:x2]

            predicted_digit = process_cell(cell, model)
            row_list.append(predicted_digit)

        sudoku_grid.append(row_list)

    return sudoku_grid

def load_model(model_path):
    try:
        model = tf.keras.models.load_model(model_path)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None
    return model

