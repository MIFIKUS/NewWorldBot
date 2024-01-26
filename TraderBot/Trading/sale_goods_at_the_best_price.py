from TraderBot.Calculation.price_calculation import PriceCalculation
from TraderBot.GoogleInfo.google_tables import GetInfo
from TraderBot.NavigationInTheGame.navigation_in_the_buy_tab import navigation_in_the_buy
from TraderBot.Parsing.parse_inventory import parse_inventory
from TraderBot.Parsing.parse_buy_order import parse_buy_order


class SaleGoodsAtTheBestPrice:
    def __init__(self):
        self.items_for_sale = None

    def quantity_comparison(self):
        inventory = parse_inventory.converting_images_to_strings()

        get_info = GetInfo(num_of_sheet=4)
        list_of_purchase_orders = [[x, y] for x, y in zip(get_info.get_value_list(1)[1:], get_info.get_value_list(4)[1:])]

        comparison = [x for x in inventory for y in list_of_purchase_orders if x[0] == y[0] and int(x[1]) >= int(y[1]) / 2]
        if len(comparison) > 0:
            self.items_for_sale = comparison
            self.movement_of_goods()
        else:
            pass

    def movement_of_goods(self):
        for i, count in range(len(self.items_for_sale)), self.items_for_sale:
            navigation_in_the_buy.go_to_buy_refined_resources()
            navigation_in_the_buy.go_to_category(self.items_for_sale[i][0])
            navigation_in_the_buy.click_to_place_sell_order()
            self.buy_products(self.calculation_of_favorable_price(self.parsing_products()), int(count[1]) / 2)

    @staticmethod
    def parsing_products(self):
        parse_buy_order.need_for_parsing_one_product = True
        price = [sublist[2] for sublist in parse_buy_order.check_count_of_goods()]
        quantity = [sublist[3] for sublist in parse_buy_order.check_count_of_goods()]
        return price, quantity

    @staticmethod
    def calculation_of_favorable_price(self, parsed_goods):
        current_price = PriceCalculation.calculations_for_one_product(parsed_goods[0], parsed_goods[1])
        return current_price

    @staticmethod
    def buy_products(self, current_price, quantity):
        navigation_in_the_buy.click_to_place_sell_order()
        navigation_in_the_buy.move_to_sell_unit_price_and_set_price(current_price)
        navigation_in_the_buy.move_to_sell_quantity_and_set_quantity(quantity)


sale_goods_at_the_best_price = SaleGoodsAtTheBestPrice()

