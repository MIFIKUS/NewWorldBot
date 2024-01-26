from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
from MainClasses.MouseAndKeyboard.keyboard_actions import Keyboard
import json

with open("E:\\projects\\NewWorldBot\\TraderBot\\Jsons\\categories_cords.json", 'r', encoding='utf-8') as data:
    categories = json.load(data)


class NavigationInBuy(Mouse, Keyboard):
    def go_to_buy_resources(self):
        self.move_and_click(230, 160)
        self.move_and_click(115, 600)

    def buy_back(self):
        self.move_and_click(250, 320)

    def click_to_buy_resources(self):
        self.move_and_click(130, 600)

    def go_to_buy_refined_resources(self):
        self.move_and_click(235, 635)

    def go_to_category(self, category):

        main_keys = [categories[main_keys] for main_keys in categories if
                     category in categories[main_keys]['categories']]
        value = main_keys[0]['categories'][category], main_keys[0]['cords']
        print(category)
        self.move_and_click(value[1][0], value[1][1]), self.move_and_click(value[0][0], value[0][1])

    def click_to_place_buy_order(self):
        self.move_and_click(380, 490)

    def click_to_place_sell_order(self):
        self.move_and_click(372, 547)

    def move_to_buy_quantity_and_set_quantity(self, quantity):
        self.move(680, 383)
        self.click()
        self.click()
        self.type(str(quantity / 2))
        print("Настоящее количество которое бот бы ввел: ", str(quantity))

    def move_to_buy_unit_price_and_set_price(self, price):
        self.move(726, 301)
        self.click()
        self.click()
        self.type(str(price))

    def move_to_sell_unit_price_and_set_price(self, price):
        self.move(726, 401)
        self.click()
        self.click()
        self.type(str(price))

    def move_to_sell_quantity_and_set_quantity(self, quantity):
        self.move(680, 610)
        self.click()
        self.click()
        self.type(quantity)

    def click_to_confirm_buy(self):
        self.move_and_click(1110, 940)


navigation_in_the_buy = NavigationInBuy()
