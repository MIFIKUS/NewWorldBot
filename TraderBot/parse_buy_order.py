from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
from MainClasses.Windows.windows import Windows
from MainClasses.Image.image import Image

import time
import json

from TraderBot.write_in_sheets import WriteInSheets

windows = Windows()
mouse = Mouse()
image = Image()


with open("E:\\projects\\NewWorldBot\\TraderBot\\Jsons\\categories_cords.json", 'r', encoding='utf-8') as data:
    categories = json.load(data)


class ParseBuyOrder:
    def __init__(self):
        self.main_categories = categories.keys()

    def start(self):
        windows.switch_windows(self.get_categories)

    def get_categories(self, hwnd):
        time.sleep(2)
        mouse.move_and_click(220, 150)
        time.sleep(1)
        mouse.move_and_click(125, 600)
        time.sleep(1)
        mouse.move_and_click(300, 640)

        for i in self.main_categories:
            category_dict = categories.get(i)
            category_cords = category_dict.get("cords")

            mouse.move_and_click(category_cords[0], category_cords[1])

            sub_categories = category_dict.get("categories")
            for sub_category_name, sub_category_cords in sub_categories.items():
                time.sleep(1)
                mouse.move_and_click(sub_category_cords[0], sub_category_cords[1])
                self.check_count_of_goods(i, sub_category_name)

            mouse.move_and_click(260, 310)

    def check_count_of_goods(self, main_name, name):
        mouse.move(1800, 288)
        time.sleep(2.2)
        image.take_screenshot("E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\arrow.png",
                              (1803, 226, 1804, 227))
        color = image.get_main_color("E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\arrow.png")

        if color == (145, 127, 97):
            self.parse_if_20(main_name, name)
        elif 50 <= color[0] <= 90 and 40 <= color[1] <= 80 and 30 <= color[2] <= 65:
            self.parse_if_not_20(main_name, name)

    def parse_if_not_20(self, main_name, name):
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
                    write_in_sheets = WriteInSheets(main_name, name, product, 0, True)
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
                    write_in_sheets = WriteInSheets(main_name, name, scroll, 0, True)
                    write_in_sheets.image_preparation()
                    break

        elif scroll > 18:
            self.parse_if_20(main_name, name, cycle=20 - scroll, number_of_entries=scroll)

    def parse_if_20(self, main_name, name, cycle=0, number_of_entries=19):
        mouse.move(1802, 298)
        num = 0

        for a in range(3):
            time.sleep(3)
            if a < 2:
                for i in range(9):
                    num += 1
                    image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\price{num}.png",
                                          (990, 345 + 77 * i, 1130, 380 + 77 * i))
                    image.take_screenshot(f"E:\\projects\\NewWorldBot\\TraderBot\\images\\screenshots\\avail{num}.png",
                                          (1695, 345 + 77 * i, 1775, 380 + 77 * i))

                    if cycle == 1 and i == 8 and a < 1:
                        mouse.move(1849, 318)
                        mouse.drag(1849, 700)
                        mouse.move(1802, 298)
                        time.sleep(1)
                    elif cycle == 0 and i == 8:
                        mouse.scroll_down(13)
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
        write_in_sheets = WriteInSheets(main_name, name, number_of_entries, 0,  True)
        write_in_sheets.image_preparation()


parse_buy_order = ParseBuyOrder()






