from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
from MainClasses.Windows.windows import Windows
from MainClasses.Image.image import Image
from MainClasses.GoogleSheets.google_sheets import GoogleSheets

import time


google_sheets = GoogleSheets("https://docs.google.com/spreadsheets/d/1nFUIPW6nUTc5CfMroHsCCKzlOG4-9rEZGVmSHc9zMog/edit#gid=0",
                             "E:\\projects\\NewWorldBot\\services_files\\credentials.json")
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
                image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{num}.png",
                                 (985, 315 + 77 * i, 1145, 400 + 77 * i))
                image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{num}.png",
                                 (1690, 315 + 77 * i, 1790, 400 + 77 * i))
                if i == 8:
                    mouse.scroll_down(13)
        if a == 2:
            for b in range(2):

                num += 1
                mouse.scroll_down(2)
                image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{num}.png",
                                      (985, 900 + 77 * b, 1145, 985 + 77 * b))
                image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{num}.png",
                                      (1690, 900 + 77 * b, 1790, 985 + 77 * b))
    write_in_sheets()


def write_in_sheets():
    for i in range(1, 21):
        price = image.image_to_string(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{i}.png", True)
        avail = image.image_to_string(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{i}.png", True)
        google_sheets.write_google({f"C{i}": price})
        google_sheets.write_google({f"D{i}": avail})


write_in_sheets()
#start()
