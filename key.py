import keyboard
import os
os.system("start render.py")
def main():
    def on_key_event(event):
        with open("key.txt", 'w') as log_file:
            log_file.write(event.name)
    keyboard.on_press(on_key_event)
    keyboard.wait('esc')
    with open("key.txt", 'w') as log_file:
        log_file.write("esc")

if __name__ == "__main__":
    main()
