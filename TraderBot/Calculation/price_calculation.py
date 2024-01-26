from TraderBot.GoogleInfo.google_tables import GetInfo, WriteInfo


class PriceCalculation:
    def __init__(self, max_price, percent):
        self.max_price = max_price
        self.percent = percent

    @staticmethod
    def search_for_optimal_price(num_of_list):
        counter = 0
        count_of_goods = 0

        get_info = GetInfo(num_of_sheet=num_of_list)

        list_of_names = get_info.get_value_list(2)[1:]
        list_of_price = get_info.get_value_list(3)[1:]
        list_of_count = get_info.get_value_list(4)[1:]

        list_of_values = {}

        for elements_of_column in list_of_names:
            total_sum = 0
            if counter > 2 and list_of_names[counter - 1] != list_of_names[counter]:

                for elements_of_category in range(counter):
                    price = float('.'.join(list_of_price[count_of_goods].replace(',', '.').replace(' ', '').split('.')[:2]))
                    amount = float(
                        '.'.join(list_of_count[count_of_goods].replace(',', '.').replace(' ', '').split('.')[:2]))
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
        list_of_values = []
        for elements_of_category in range(len(price)):

            if '.' in price[elements_of_category]:
                prices = float('.'.join(price[elements_of_category].replace(',', '.').replace(' ', '').split('.')[:2]))
            else:
                prices = int(price[elements_of_category])

            if '.' in count[elements_of_category]:
                amount = float('.'.join(count[elements_of_category].replace(',', '.').replace(' ', '').split('.')[:2]))
            else:
                amount = float(count[elements_of_category])

            product = prices * amount
            total_sum += product

            if total_sum > 1000:
                return prices - 0.01

    def counting_quantity(self, cost_of_good):
        number_of_multiplications = self.max_price / cost_of_good
        quantity = number_of_multiplications - (number_of_multiplications / 100) * 2.5 - 1

        return quantity

    def calculating_price_difference(self):
        buy_order = self.search_for_optimal_price(3)
        sell_order = self.search_for_optimal_price(0)

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
        write_info = WriteInfo(num_of_sheet=4)
        write_info.write_list_of_values('Покупка/Продажа!A2', self.calculating_price_difference())



