Python
from pynput.keyboard import Key, Listener

def on_press(key):
    # Logging the pressed key to the console
    try:
        print(f'Key pressed: {key.char}')
    except AttributeError:
        print(f'Special key pressed: {key}')

# Setting up the listener
with Listener(on_press=on_press) as listener:
    listener.join()
