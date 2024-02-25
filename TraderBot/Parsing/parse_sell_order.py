from TraderBot.DataBase.write_to_db import write_to_db
from TraderBot.Parsing.parse_buy_order import image, mouse
from TraderBot.PhotoPreparation.photo_preparation import PhotoPreparation, list_of_values
from TraderBot.Preparations.preparing_to_write_to_database import PreparingToWriteToDatabase
from TraderBot.Jsons.get_json_data import get_json
from TraderBot.shared_variables import path_to_screenshots
import TraderBot.shared_variables as shared_variables

import time


class ParseSellOrder:

    def get_categories(self):
        categories = get_json()
        time.sleep(2)
        mouse.move_and_click(570, 150)
        time.sleep(1)
        mouse.move_and_click(670, 230)
        time.sleep(1)
        mouse.move_and_click(140, 670)

        for i in categories.keys():
            category_dict = categories.get(i)
            category_cords = category_dict.get("main category cords")
            mouse.move_and_click(category_cords[0], category_cords[1] + 65)
            sub_categories = category_dict.get("category_of_goods")
            for sub_category_name, sub_category_cords in sub_categories.items():
                mouse.move_and_click(sub_category_cords.get('cords')[0], sub_category_cords.get('cords')[1] + 65)
                for name_of_category, cords_of_category in sub_category_cords.get('categories').items():
                    mouse.move_and_click(cords_of_category[0], cords_of_category[1] + 65)

                    time.sleep(2.3)
                    if self.check_for_availability_of_goods() is False:
                        mouse.move_and_click(260, 390)
                        continue

                    self.parse_products(sub_category_name, name_of_category)

                mouse.move_and_click(260, 390)
            mouse.move_and_click(260, 390)

        write_to_db.recording_orders(shared_variables.character_id, 'buy_orders',
                                     PreparingToWriteToDatabase.preparing_list_for_orders(list_of_values))

    def check_for_availability_of_goods(self):
        image.take_screenshot(shared_variables.path_to_screenshots + 'refresh.png', (1218, 714, 1219, 722))
        a = image.get_main_color(shared_variables.path_to_screenshots + 'refresh.png')
        if a[0] > 85 and a[1] > 85 and a[2] > 85:
            return False
        return True

    def parse_products(self, main_name, name):
        count_of_goods = 0
        time.sleep(2.5)
        for count_of_goods in range(10):
            image.take_screenshot(path_to_screenshots + f"pic{count_of_goods}.png",
                                  (630, 385 + 77 * count_of_goods, 685, 435 + 77 * count_of_goods))

            if (count_of_goods > 0 and
                    image.matching(
                        path_to_screenshots + f"pic{count_of_goods - 1}.png",
                        path_to_screenshots + f"pic{count_of_goods}.png")
                    is False):
                count_of_goods = count_of_goods
                break
        for product in range(count_of_goods):

            image.take_screenshot(path_to_screenshots + f"price{product + 1}.png",
                                  (990, 385 + 77 * product, 1130, 435 + 77 * product))
            image.take_screenshot(path_to_screenshots + f"avail{product + 1}.png",
                                  (1680, 385 + 77 * product, 1750, 435 + 77 * product))

            if product == count_of_goods - 1:
                write_in_sheets = PhotoPreparation(main_name, name, product + 1)
                write_in_sheets.image_preparation()
                break
        mouse.move_and_click(260, 390)


parse_sell_order = ParseSellOrder()

