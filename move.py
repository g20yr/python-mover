import pyautogui
import time
import random

def move_mouse_randomly():
    # Get the size of the screen
    screenWidth, screenHeight = pyautogui.size()
    # Generate random x and y coordinates
    x = random.randint(0, screenWidth - 1)
    y = random.randint(0, screenHeight - 1)
    # Choose a random duration for the movement (smooth movement)
    duration = random.uniform(0.5, 2.0)
    print(f"Moving mouse to ({x}, {y}) over {duration:.2f} seconds.")
    pyautogui.moveTo(x, y, duration=duration)

def press_random_key():
    # List of keys that can be pressed; you can add more as needed
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    key = random.choice(keys)
    print(f"Pressing key: {key}")
    pyautogui.press(key)

def main():
    try:
        while True:
            # Wait for an irregular interval between 2 and 10 seconds
            interval = random.uniform(2, 10)
            print(f"Waiting for {interval:.2f} seconds...")
            time.sleep(interval)
            # Randomly choose an action: move, key, or both
            action = random.choice(['move', 'key', 'both'])
            if action == 'move':
                move_mouse_randomly()
            elif action == 'key':
                press_random_key()
            elif action == 'both':
                move_mouse_randomly()
                press_random_key()
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == '__main__':
    main()
