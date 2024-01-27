from datetime import datetime
import time

from pynput.mouse import Listener, Button, Controller
import pandas as pd
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Define the directory path from environment variable
directory = os.getenv('MOUSE_TRAINING_DIR')



# Check if the directory exists, and create it if it doesn't
if not os.path.exists(directory):
    os.makedirs(directory)

# Initialize a list to store mouse events
mouse_data = []

def write_data():
    """Writes the data to the CSV file."""
    with open(filename, 'a') as file:
        for line in mouse_data:
            file.write(line + '\n')
    mouse_data.clear()

def on_move(x, y):
    mouse_data.append(f'{x}, {y}, {time.time() % (60*60*24)}, 0')
    print(f'{x}, {y}, {time.time()%(60*60*24)}, 0')
    if len(mouse_data) >= 100:  # Adjust this number based on your preference
        write_data()

def on_click(x, y, button, pressed):
    if pressed:
        mouse_data.append(f'{x}, {y}, {time.time() % (60*60*24)}, 1')
        print(f'{x}, {y}, {time.time()%(60*60*24)}, 1')
        if len(mouse_data) >= 100:  # Adjust this number based on your preference
            write_data()

def listen():
    with Listener(on_move=on_move, on_click=on_click) as listener:
        listener.join()

if __name__ == '__main__':
    listen()
    write_data()  # Ensure any remaining data is written when the script stops
