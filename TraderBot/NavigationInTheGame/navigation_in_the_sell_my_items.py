from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
from MainClasses.MouseAndKeyboard.keyboard_actions import Keyboard
import json

with open("E:\\projects\\NewWorldBot\\TraderBot\\Jsons\\categories_cords.json", 'r', encoding='utf-8') as data:
    categories = json.load(data)


class NavigationInSellMyItems(Mouse, Keyboard):
    def go_to_my_items(self):
        self.move_and_click(535, 155)
        self.move_and_click(325, 230)


navigation_in_the_sell_my_items = NavigationInSellMyItems()





#668,311
#677, 1038