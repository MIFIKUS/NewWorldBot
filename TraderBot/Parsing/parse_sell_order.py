from TraderBot.DataBase.write_to_db import write_to_db
from TraderBot.Parsing.parse_buy_order import image, mouse
from TraderBot.PhotoPreparation.photo_preparation import PhotoPreparation, list_of_values
from TraderBot.Jsons.get_json_data import GetJsonData
from TraderBot.NavigationInTheGame.navigation_in_the_characters_menu import NavigationInCharactersMenu

import time


class ParseSellOrder:
    def __init__(self):
        self.categories = GetJsonData.get_json()

    def get_categories(self):
        time.sleep(2)
        mouse.move_and_click(570, 150)
        time.sleep(1)
        mouse.move_and_click(670, 230)
        time.sleep(1)
        mouse.move_and_click(140, 670)
        time.sleep(1)
        mouse.move_and_click(300, 720)

        for i in self.categories.keys():
            category_dict = self.categories.get(i)
            category_cords = category_dict.get("main category cords")
            mouse.move_and_click(category_cords[0], category_cords[1] + 65)
            sub_categories = category_dict.get("category_of_goods")
            for sub_category_name, sub_category_cords in sub_categories.items():
                mouse.move_and_click(sub_category_cords.get('cords')[0], sub_category_cords.get('cords')[1] + 65)
                for name_of_category, cords_of_category in sub_category_cords.get('categories').items():
                    mouse.move_and_click(cords_of_category[0], cords_of_category[1] + 65)

                    self.parse_products(sub_category_name, name_of_category)

                mouse.move_and_click(260, 390)

        write_to_db.recording_orders(NavigationInCharactersMenu().character_id, 'buy_orders', list_of_values)

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
                write_in_sheets = PhotoPreparation(main_name, name, product + 1)
                write_in_sheets.image_preparation()
                break
        mouse.move_and_click(260, 390)


parse_sell_order = ParseSellOrder()

