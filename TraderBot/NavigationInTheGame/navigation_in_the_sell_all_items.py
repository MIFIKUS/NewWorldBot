from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
from MainClasses.MouseAndKeyboard.keyboard_actions import Keyboard
import json

with open("E:\\projects\\NewWorldBot\\TraderBot\\Jsons\\categories_cords.json", 'r', encoding='utf-8') as data:
    categories = json.load(data)


class NavigationInSellAllItems(Mouse, Keyboard):

    def go_to_sell_resources(self):
        self.move_and_click(535, 155)
        self.move_and_click(745, 225)
        self.move_and_click(150, 680)

    def sell_back(self):
        self.move_and_click(260, 395)


navigation_in_sell_all_items = NavigationInSellAllItems()

