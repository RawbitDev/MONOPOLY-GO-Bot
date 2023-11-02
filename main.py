import os
import time
import random
import pyautogui as pag


def random_timeout():
    timeout = random.uniform(0.1, 0.5)
    time.sleep(timeout)


def get_center_xy(box):
    center = pag.center(box)
    x, y = center
    return x, y


if __name__ == '__main__':
    buttons_dir = "./buttons/"
    buttons_files = os.listdir(buttons_dir)
    print(f'\nStarting to searching for buttons {buttons_files}')
    while True:
        for button_file in buttons_files:
            button_path = os.path.join(buttons_dir, button_file)
            button_name = button_file.split(".")[0]
            try:
                buttons_gen = pag.locateAllOnScreen(button_path, grayscale=True, confidence=0.9)
                buttons = [get_center_xy(x) for x in buttons_gen]
                if len(buttons) >= 1:
                    print(f'\nFound button "{button_name}" at {buttons}')
                    button = buttons[0]
                    if len(buttons) >= 1:
                        button = random.choice(buttons)
                        print(f' > Randomly chosen button at {button}')
                    x, y = button
                    pag.click(x, y)
                    print(f' > Clicked it!')
                    random_timeout()
            except Exception as e:
                print(e)
                pass