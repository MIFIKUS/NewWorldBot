from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
import json

with open("E:\\projects\\NewWorldBot\\TraderBot\\Jsons\\categories_cords.json", 'r', encoding='utf-8') as data:
    categories = json.load(data)

class NavigationInSell(Mouse):

    def go_to_sell_resources(self):
        self.move_and_click(535, 155)
        self.move_and_click(745, 225)
        self.move_and_click(150, 680)

    def sell_back(self):
        self.move_and_click(260, 395)


class NavigationInBuy(Mouse):
    def go_to_buy_resources(self):
        self.move_and_click(230, 160)
        self.move_and_click(250, 145)
        self.move_and_click(130, 600)

    def buy_back(self):
        self.move_and_click(250, 320)

    def go_to_buy_refined_resources(self):
        self.move_and_click(235, 635)

    def go_to_category(self, category):

        main_keys = [categories[main_keys] for main_keys in categories if
                     category in categories[main_keys]['categories']]
        value = main_keys[0]['categories'][category], main_keys[0]['cords']

        self.move(value[0][0], value[0][1]), self.move(value[1][0], value[1][1])

    def click_to_place_buy_order(self):
        self.move_and_click(380, 482)

    def move_to_buy_quantity(self):
        self.move(680, 383)

    def move_to_buy_unit_price(self):
        self.move(726, 301)

    def click_to_confirm_buy(self):
        self.move_and_click(1110, 940)


navigation_in_the_buy = NavigationInBuy()
#navigation_in_the_buy.go_to_category("Timber")
