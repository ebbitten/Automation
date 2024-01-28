from datetime import datetime
import time
import os
from pynput.mouse import Listener
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Define the directory path from the environment variable
directory = os.getenv('MOUSE_TRAINING_DIR')

# Check if the directory exists, and create it if it doesn't
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the filename for storing data
filename = os.path.join(directory, f'{datetime.today().strftime("%d_%m_%Y")}.csv')

# Initialize a list to store mouse events
mouse_data = []

def write_data():
    """Writes the data to the CSV file."""
    global mouse_data  # Declare mouse_data as global to modify it
    with open(filename, 'a') as file:
        for line in mouse_data:
            file.write(line + '\n')
    mouse_data.clear()

def on_move(x, y):
    """Handles the on_move event."""
    mouse_data.append(f'{x}, {y}, {time.time() % (60*60*24)}, 0')
    print(f'{x}, {y}, {time.time() % (60*60*24)}, 0')
    if len(mouse_data) >= 100:  # Adjust this number based on your preference
        write_data()

def on_click(x, y, button, pressed):
    """Handles the on_click event."""
    if pressed:
        mouse_data.append(f'{x}, {y}, {time.time() % (60*60*24)}, 1')
        print(f'{x}, {y}, {time.time() % (60*60*24)}, 1')
        if len(mouse_data) >= 100:  # Adjust this number based on your preference
            write_data()

def listen():
    """Starts the mouse event listener."""
    with Listener(on_move=on_move, on_click=on_click) as listener:
        listener.join()

if __name__ == '__main__':
    listen()
    write_data()  # Ensure any remaining data is written when the script stops
