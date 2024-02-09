from TraderBot.DataBase.write_to_db import write_to_db
from TraderBot.DataBase.read_db import read_db
from TraderBot.NavigationInTheGame.navigation_in_the_characters_menu import NavigationInCharactersMenu


class PriceCalculation:
    def __init__(self, max_price, percent):
        self.max_price = max_price
        self.percent = percent

    @staticmethod
    def search_for_optimal_price(name_of_list):
        counter = 0
        count_of_goods = 0

        list_of_names = [x[1] for x in read_db.get_data_from_table_of_orders(NavigationInCharactersMenu().character_id,
                                                                             name_of_list)]
        list_of_price = [x[2] for x in read_db.get_data_from_table_of_orders(NavigationInCharactersMenu().character_id,
                                                                             name_of_list)]
        list_of_count = [x[3] for x in read_db.get_data_from_table_of_orders(NavigationInCharactersMenu().character_id,
                                                                             name_of_list)]
        list_of_values = {}

        for _ in list_of_names:
            total_sum = 0
            if counter > 2 and list_of_names[counter - 1] != list_of_names[counter]:

                for elements_of_category in range(counter):
                    price = list_of_price[count_of_goods]
                    amount = list_of_count[count_of_goods]
                    product = price * amount
                    total_sum += product

                    if total_sum > 1000:
                        list_of_values.update({list_of_names[count_of_goods]: price})
                        count_of_goods = counter
                        break

                    count_of_goods += 1
            counter += 1

        return list_of_values

    @staticmethod
    def calculations_for_one_product(price, count):
        total_sum = 0
        for elements_of_category in range(len(price)):
            product = price[elements_of_category] * count[elements_of_category]
            total_sum += product

            if total_sum > 1000:
                return price[elements_of_category] - 0.01

    def counting_quantity(self, cost_of_good):
        number_of_multiplications = self.max_price / cost_of_good
        quantity = number_of_multiplications - (number_of_multiplications / 100) * 2.5 - 1

        return quantity

    def calculating_price_difference(self):
        buy_order = self.search_for_optimal_price('buy_orders')
        sell_order = self.search_for_optimal_price('sell_orders')

        characters = {}

        if buy_order.keys() != sell_order.keys():
            for key1 in buy_order:
                if key1 not in sell_order:
                    sell_order[key1] = buy_order[key1] * 2

            for key2 in sell_order:
                if key2 not in buy_order:
                    buy_order[key2] = sell_order[key2] - sell_order[key2] * 0.7

        for key in buy_order:
            characters[key] = [buy_order[key], sell_order[key]]

        for key in list(characters.keys()):
            diff = int((characters[key][1] - characters[key][0]) / buy_order[key] * 100)
            if diff < self.percent:
                del characters[key]
                continue

            characters[key].append(self.counting_quantity(characters[key][0]))
            characters[key].append(diff)

        dictionary = [[key, *value] for key, value in characters.items()]
        sorted_data = sorted(dictionary, key=lambda x: x[-1], reverse=True)

        return sorted_data

    def record_price_difference_in_table(self):
        write_to_db.record_purchase_and_sale_prices(NavigationInCharactersMenu().character_id,
                                                    self.calculating_price_difference())



