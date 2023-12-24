from parse_buy_order import windows, image, mouse
from write_in_sheets import WriteInSheets
import json
import time

with open("E:\\projects\\NewWorldBot\\TraderBot\\Jsons\\catigories_cords.json", 'r', encoding='utf-8') as data:
    categories = json.load(data)


class ParseSellOrder:
    def __init__(self):
        self.main_categories = categories.keys()

    def start(self):
        windows.switch_windows(self.get_categories)

    def get_categories(self, hwnd):
        time.sleep(2)
        mouse.move_and_click(570, 150)
        time.sleep(1)
        mouse.move_and_click(670, 230)
        time.sleep(1)
        mouse.move_and_click(140, 670)
        time.sleep(1)
        mouse.move_and_click(300, 720)

        for i in self.main_categories:
            category_dict = categories.get(i)
            category_cords = category_dict.get("cords")

            mouse.move_and_click(category_cords[0], category_cords[1] + 65)

            sub_categories = category_dict.get("categories")
            for sub_category_name, sub_category_cords in sub_categories.items():
                time.sleep(1)
                mouse.move_and_click(sub_category_cords[0], sub_category_cords[1] + 60)
                self.parse_products(i, sub_category_name)

            mouse.move_and_click(260, 390)

    def parse_products(self, main_name, name):
        count_of_goods = 0
        time.sleep(2.5)
        for count_of_goods in range(10):
            image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\pic{count_of_goods}.png",
                                  (630, 385 + 77 * count_of_goods, 685, 435 + 77 * count_of_goods))

            if (count_of_goods > 0 and
                    image.matching(
                        f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\pic{count_of_goods - 1}.png",
                        f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\pic{count_of_goods}.png")
                    is False):
                count_of_goods = count_of_goods
                break
        for product in range(count_of_goods):

            image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{product + 1}.png",
                                  (990, 385 + 77 * product, 1130, 435 + 77 * product))
            image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{product + 1}.png",
                                  (1680, 385 + 77 * product, 1750, 435 + 77 * product))

            if product == count_of_goods - 1:
                write_in_sheets = WriteInSheets(main_name, name, product + 1, 3)
                write_in_sheets.image_preparation()
                break
        mouse.move_and_click(260, 390)


parse_sell_order = ParseSellOrder()
parse_sell_order.start()
