import time

from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
from MainClasses.Windows.windows import Windows
from MainClasses.Image.image import Image

windows = Windows()
mouse = Mouse()
image = Image()

cord = (615, 315, 1780, 400)
AMOUNT_OF_PRODUCTS = 9


def start():
    windows.switch_windows(search_products)


def search_products(hwnd):
    mouse.move_and_click(125, 600)
    mouse.move_and_click(300, 640)
    mouse.move_and_click(250, 435)
    parse_products()


def parse_products():
    num = 0
    mouse.move(1800, 288)
    for a in range(3):
        time.sleep(2)
        if a < 2:

            for i in range(AMOUNT_OF_PRODUCTS):
                num += 1
                image.take_screenshot(f"TraderBot\\images\\screenshots\\price{num}.png",
                                 (985, 315 + 77 * i, 1145, 400 + 77 * i))
                image.take_screenshot(f"TraderBot\\images\\screenshots\\avail{num}.png",
                                 (1690, 315 + 77 * i, 1790, 400 + 77 * i))
                if i == 8:
                    mouse.scroll_down(13)
        if a == 2:
            for b in range(2):
                num += 1
                mouse.scroll_down(2)
                image.take_screenshot(f"TraderBot\\images\\screenshots\\price{num}.png",
                                      (985, 900 + 77 * b, 1145, 985 + 77 * b))
                image.take_screenshot(f"TraderBot\\images\\screenshots\\avail{num}.png",
                                      (1690, 900 + 77 * b, 1790, 985 + 77 * b))
    write_in_sheets()


def write_in_sheets():
    for i in range(1, 21):
        print(image.image_to_string(f"TraderBot\\images\\screenshots\\price{i}.png", True), f"Цена {i}")
        print(image.image_to_string(f"TraderBot\\images\\screenshots\\avail{i}.png", True), f"Количество {i}")

#write_in_sheets()
start()
