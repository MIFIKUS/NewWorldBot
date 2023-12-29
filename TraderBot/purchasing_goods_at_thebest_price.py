from write_in_sheets import calculating

import json


with open("/TraderBot/Jsons/categories_cords.json", 'r', encoding='utf-8') as data:
    categories = json.load(data)


class PurchasingGoodsAtTheBestPrice:

    def search_for_the_optimal_price(self):
        list_of_values = calculating()
        self.search_for_buy_button(list_of_values)

    def search_for_buy_button(self, list_of_values):
        pass


