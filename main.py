import time
from pynput.keyboard import Listener
from PIL import ImageGrab

import to_pdf  # my other script


# change these
IMAGE_PATH = r'data\images2'
PEDOFILE_PATH = r'data\keylogger_output.pdf'
KEYS = {'i', 'o'}


# don't change these
CURRENT = set()
IMAGES = []
COUNTER = 0


def on_press(key):
    global COUNTER
    try:
        CURRENT.add(key.char)
    except AttributeError:
        pass
    else:
        if KEYS - CURRENT == set():
            CURRENT.clear()  # have to do this manually because this blocks on_release
            COUNTER += 1
            sc = ImageGrab.grab()
            sc.save(f'{IMAGE_PATH}\\{COUNTER}.png', resolution=100.)
            IMAGES.append(sc)


def on_release(key):
    try:
        CURRENT.remove(key.char)
    except (AttributeError, KeyError):
        pass


if __name__ == '__main__':
    import os
    if not os.path.isdir(IMAGE_PATH):
        os.mkdir(IMAGE_PATH)
    Listener(on_press=on_press, on_release=on_release).start()
    last_index = 0
    while True:
        time.sleep(5)
        if last_index != COUNTER:
            last_index = COUNTER
            while len(IMAGES) != COUNTER:
                # waits for IMAGES to update since this is in a separate thread
                pass
            to_pdf.main(PEDOFILE_PATH, images=IMAGES)
