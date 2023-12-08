from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
from MainClasses.Windows.windows import Windows
from MainClasses.Image.image import Image
from MainClasses.GoogleSheets.google_sheets import GoogleSheets

import time
import json

google_sheets = GoogleSheets("https://docs.google.com/spreadsheets/d/1nFUIPW6nUTc5CfMroHsCCKzlOG4-9rEZGVmSHc9zMog/edit#gid=0",
                             "E:\\projects\\NewWorldBot\\services_files\\credentials.json")
windows = Windows()
mouse = Mouse()
image = Image()


with open("E:\\projects\\NewWorldBot\\TraderBot\\Jsons\\catigories_cords.json", 'r', encoding='utf-8') as data:
    categories = json.load(data)

main_categories = categories.keys()
cord = (615, 315, 1780, 400)
AMOUNT_OF_PRODUCTS = 9
cell_num = 2
end_sell = 0


def start():
    windows.switch_windows(search_products)


def search_products(hwnd):
    time.sleep(1)
    mouse.move_and_click(125, 600)
    time.sleep(1)
    mouse.move_and_click(300, 640)

    for i in main_categories:
        category_dict = categories.get(i)
        category_cords = category_dict.get("cords")

        mouse.move_and_click(category_cords[0], category_cords[1])

        sub_categories = category_dict.get("categories")

        for sub_category_name, sub_category_cords in sub_categories.items():
            time.sleep(1)
            mouse.move_and_click(sub_category_cords[0], sub_category_cords[1])
            parse_products(i, sub_category_name)


def parse_products(main_name, name):
    num = 0
    mouse.move(1800, 288)
    for a in range(3):
        time.sleep(3)
        if a < 2:

            for i in range(AMOUNT_OF_PRODUCTS):
                num += 1
                image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{num}.png",
                                 (995, 315 + 77 * i, 1135, 400 + 77 * i))
                image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{num}.png",
                                 (1700, 315 + 77 * i, 1780, 400 + 77 * i))
                if i == 8:
                    mouse.scroll_down(13)
        if a == 2:
            for b in range(2):

                num += 1
                mouse.scroll_down(2)
                image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{num}.png",
                                      (995, 900 + 77 * b, 1135, 985 + 77 * b))
                image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{num}.png",
                                      (1700, 900 + 77 * b, 1780, 985 + 77 * b))

    mouse.move_and_click(260, 310)
    write_in_sheets(main_name, name)


def write_in_sheets(main_name, name):
    global cell_num
    global end_sell
    price_list = []
    avail_list = []
    main_name_list = []
    name_list = []
    for i in range(1, 21):

        image.delete_all_colors_except_one(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{i}.png",
                                           [96, 86, 69], [166, 156, 140])
        image.delete_all_colors_except_one(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{i}.png",
                                           [96, 86, 69], [166, 156, 140])
        price = image.image_to_string(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{i}.png",
                                      True)
        avail = image.image_to_string(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{i}.png",
                                      True)
        price_list.append([price])
        avail_list.append([avail])
        main_name_list.append([main_name])
        name_list.append([name])
        end_sell += 1

    google_sheets.write_google({f"A{cell_num}:A{end_sell+1}": main_name_list})
    google_sheets.write_google({f"B{cell_num}:B{end_sell+1}": name_list})
    google_sheets.write_google({f"C{cell_num}:C{end_sell+1}": price_list})
    google_sheets.write_google({f"D{cell_num}:D{end_sell+1}": avail_list})
    cell_num = end_sell + 1


#write_in_sheets("Refined woods", "Timber")
start()
#search_products(None)
