from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
from MainClasses.Image.image import Image
from TraderBot.PhotoPreparation.photo_preparation import PhotoPreparation
from TraderBot.PhotoPreparation.photo_preparation import list_of_values #, list_of_uniq_values
from TraderBot.Jsons.get_json_data import GetJsonData
from TraderBot.DataBase.write_to_db import write_to_db
from TraderBot.NavigationInTheGame.navigation_in_the_characters_menu import NavigationInCharactersMenu

import time

mouse = Mouse()
image = Image()


class ParseBuyOrder:
    def __init__(self, need_for_parsing_one_product=False):
        self.need_for_parsing_one_product = need_for_parsing_one_product
        self.name_of_category = None
        self.name_of_goods = None
        self.categories = GetJsonData.get_json()

    def get_categories(self):
        time.sleep(1)
        mouse.move_and_click(220, 150)
        mouse.move_and_click(125, 600)

        for i in self.categories.keys():
            category_dict = self.categories.get(i)
            category_cords = category_dict.get("main category cords")
            mouse.move_and_click(category_cords[0], category_cords[1])
            sub_categories = category_dict.get("category_of_goods")

            for sub_category_name, sub_category_cords in sub_categories.items():
                self.name_of_category = sub_category_name
                mouse.move_and_click(sub_category_cords.get('cords')[0], sub_category_cords.get('cords')[1])
                for name_of_category, cords_of_category in sub_category_cords.get('categories').items():
                    mouse.move_and_click(cords_of_category[0], cords_of_category[1])

                    self.name_of_category = name_of_category
                    self.check_count_of_goods()

                mouse.move_and_click(260, 310)

        write_to_db.recording_orders(NavigationInCharactersMenu().character_id, 'sell_orders', list_of_values)

    def check_count_of_goods(self):
        mouse.move(1800, 288)
        time.sleep(2.2)
        image.take_screenshot("E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\arrow.png",
                              (1803, 226, 1804, 227))
        color = image.get_main_color("E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\arrow.png")

        if color == (145, 127, 97):
            self.parse_if_20()
        elif 50 <= color[0] <= 90 and 40 <= color[1] <= 80 and 30 <= color[2] <= 65:
            self.parse_if_not_20()

        if self.need_for_parsing_one_product is True:
            return list_of_values

    def parse_if_not_20(self):
        def check_scrollbar():
            mouse.move(1800, 288)
            image.take_screenshot("E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\is_there_a_scroll.png",
                                  (1842, 320, 1848, 338))
            scroll_color = image.get_main_color(
                "E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\is_there_a_scroll.png")

            if 0 <= scroll_color[0] <= 55 and 0 <= scroll_color[1] <= 55 and 0 <= scroll_color[2] <= 55:
                return 9

            elif 60 <= scroll_color[0] <= 140 and 60 <= scroll_color[1] <= 140 and 60 <= scroll_color[2] <= 140:
                scroll_cords = (
                (1841, 664, 1850, 681), (1841, 682, 1850, 701), (1841, 702, 1850, 724), (1841, 725, 1850, 750),
                (1841, 751, 1850, 778), (1841, 779, 1850, 811), (1841, 812, 1850, 849), (1841, 850, 1850, 894),
                (1841, 895, 1850, 946), (1841, 947, 1850, 1009), (1841, 1010, 1850, 1039))

                for number, i in enumerate(scroll_cords):
                    image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\"
                                          f"screenshots\\scroll_count.png", i)
                    scroll_cords_color = image.get_main_color(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\"
                                                              f"screenshots\\scroll_count.png")

                    if 0 <= scroll_cords_color[0] <= 75 and 0 <= scroll_cords_color[1] <= 75 and 0 <= scroll_cords_color[
                        2] <= 75:
                        return 20 - number

        scroll = check_scrollbar()

        if scroll == 9:
            count_of_goods = 0
            for count_of_goods in range(10):
                image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\pic{count_of_goods}.png",
                                      (630, 326 + 77 * count_of_goods, 685, 386 + 77 * count_of_goods))

                if (count_of_goods > 0 and
                        image.matching(
                            f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\pic{count_of_goods - 1}.png",
                            f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\pic{count_of_goods}.png")
                        is False):
                    count_of_goods = count_of_goods
                    break
            for product in range(count_of_goods):

                image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{product + 1}.png",
                                      (990, 345 + 77 * product, 1130, 375 + 77 * product))
                image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{product + 1}.png",
                                      (1695, 345 + 77 * product, 1775, 375 + 77 * product))
                if product == count_of_goods - 1:
                    mouse.move_and_click(260, 310)
                    write_in_sheets = PhotoPreparation(self.name_of_category, self.name_of_goods, product, True)
                    write_in_sheets.image_preparation()
                    break

        elif 9 < scroll < 19:
            count_of_goods = 0
            for item_of_goods in range(scroll):
                count_of_goods += 1
                image.take_screenshot(
                    f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{count_of_goods}.png",
                    (990, 345 + 77 * item_of_goods, 1130, 375 + 77 * item_of_goods))
                image.take_screenshot(
                    f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{count_of_goods}.png",
                    (1695, 345 + 77 * item_of_goods, 1775, 375 + 77 * item_of_goods))
                if item_of_goods == 8:
                    mouse.scroll_down_cords(2000)
                    break
            time.sleep(1)
            for products_after_scrolling in range(scroll):

                if products_after_scrolling >= 18 - scroll:
                    count_of_goods += 1

                    image.take_screenshot(
                        f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{count_of_goods}.png",
                        (990, 380 + 77 * products_after_scrolling, 1130, 415 + 77 * products_after_scrolling))
                    image.take_screenshot(
                        f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{count_of_goods}.png",
                        (1695, 380 + 77 * products_after_scrolling, 1775, 415 + 77 * products_after_scrolling))

                if products_after_scrolling == 8:
                    mouse.move_and_click(260, 310)
                    write_in_sheets = PhotoPreparation(self.name_of_category, self.name_of_goods, scroll, True)
                    write_in_sheets.image_preparation()
                    break

        elif scroll > 18:
            self.parse_if_20(cycle=20 - scroll, number_of_entries=scroll)

    def parse_if_20(self, cycle=0, number_of_entries=19):
        mouse.move(1802, 298)
        num = 0

        for a in range(3):
            if a < 2:
                for i in range(9):
                    num += 1
                    image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{num}.png",
                                          (990, 345 + 77 * i, 1130, 380 + 77 * i))
                    image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{num}.png",
                                          (1695, 345 + 77 * i, 1775, 380 + 77 * i))

                    if i == 8 and cycle == 0:
                        mouse.scroll_down(13)
                        time.sleep(1)
                    elif cycle == 1 and i == 8 and a < 1:
                        mouse.move(1849, 318)
                        mouse.drag(1849, 700)
                        mouse.move(1802, 298)
                        time.sleep(1)
                    else:
                        continue

            if a == 2:
                for b in range(2):
                    if b >= cycle:
                        num += 1
                        mouse.scroll_down(5)
                        time.sleep(1)
                        image.take_screenshot(
                            f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{num}.png",
                            (980, 920 + 77 * b, 1140, 945 + 77 * b))
                        image.take_screenshot(
                            f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{num}.png",
                            (1685, 920 + 77 * b, 1785, 945 + 77 * b))

        mouse.move_and_click(260, 310)

        write_in_sheets = PhotoPreparation(self.name_of_category, self.name_of_goods, number_of_entries)
        write_in_sheets.image_preparation()


parse_buy_order = ParseBuyOrder()


