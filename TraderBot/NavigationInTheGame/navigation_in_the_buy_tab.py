from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
from MainClasses.MouseAndKeyboard.keyboard_actions import Keyboard
from TraderBot.Jsons.get_json_data import GetJsonData

categories = GetJsonData.get_json()


class NavigationInBuy(Mouse, Keyboard):
    def go_to_buy_resources(self):
        self.move_and_click(230, 160)
        self.move_and_click(115, 600)

    def buy_back(self):
        self.move_and_click(250, 320)

    def click_to_buy_resources(self):
        self.move_and_click(130, 600)

    def go_to_buy_catalog_of_resources(self, category):
        for main in categories:
            for cats in categories.get(main)['category_of_goods'].items():
                if category == next(iter(cats[1]['categories'])):
                    self.move_and_click(categories.get(main)['main category cords'][0],
                                        categories.get(main)['main category cords'][1])

    def go_to_category(self, category):
        for main in categories:
            for cats in categories.get(main)['category_of_goods'].items():
                if category == next(iter(cats[1]['categories'])):
                    self.move_and_click(categories.get(main)['main category cords'][0],
                                        categories.get(main)['main category cords'][1])
                    self.move_and_click(cats[1]['cords'][0], cats[1]['cords'][1])
                    self.move_and_click(cats[1]['categories'][category][0], cats[1]['categories'][category][1])

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
