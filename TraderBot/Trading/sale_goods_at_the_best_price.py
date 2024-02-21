import math
import time

from TraderBot.ActionsAndChecksInGame.check import check
from TraderBot.Calculation.price_calculation import PriceCalculation
from TraderBot.DataBase.write_to_db import write_to_db
from TraderBot.NavigationInTheGame.navigation_in_the_buy_tab import navigation_in_the_buy
from TraderBot.Parsing.parse_inventory import parse_inventory
from TraderBot.Parsing.parse_buy_order import parse_buy_order
from TraderBot.DataBase.read_db import read_db
from TraderBot.shared_variables import path_to_screenshots
import TraderBot.shared_variables as shared_variables


class SaleGoodsAtTheBestPrice:
    def __init__(self):
        self.items_for_sale = None

    def quantity_comparison(self):
        inventory = parse_inventory.converting_images_to_strings()

        get_info_of_purchase_orders = read_db.get_transactions_goods(shared_variables.character_id)
        print(get_info_of_purchase_orders)
        comparison = [x for x in inventory for y in get_info_of_purchase_orders if x[0] == y[0] and int(x[1]) >= int(y[1]) / 2]
        print(comparison)

        if len(comparison) > 0:
            self.items_for_sale = comparison
            self._movement_of_goods()
        else:
            pass

    def _movement_of_goods(self):

        for i in self.items_for_sale:
            navigation_in_the_buy.go_to_buy_resources()
            navigation_in_the_buy.go_to_category(i[0])

            self._buy_products(self._calculation_of_favorable_price(self._parsing_products()), int(i[1]), i[0])

        time.sleep(1.5)

    @staticmethod
    def _parsing_products():
        parse_products = parse_buy_order.check_count_of_goods(need_for_parsing_one_product=True)
        price = [float(sublist[2]) for sublist in parse_products]
        quantity = [int(sublist[3]) for sublist in parse_products]
        return price, quantity

    @staticmethod
    def _calculation_of_favorable_price(parsed_goods):
        price_calculation = PriceCalculation(shared_variables.max_price, shared_variables.percent)
        current_price = price_calculation.calculations_for_one_product(parsed_goods[0], parsed_goods[1])
        return current_price

    def _buy_products(self, current_price, quantity, name):
        navigation_in_the_buy.go_to_buy_resources()
        navigation_in_the_buy.go_to_category(name)

        navigation_in_the_buy.click_to_place_sell_order()
        navigation_in_the_buy.move_to_sell_unit_price_and_set_price(current_price)
        navigation_in_the_buy.move_to_sell_quantity_and_set_quantity(quantity)

        time.sleep(1.3)
        if 60 <= check.check_for_red()[0]:
            self.selling_by_occult_means(name, quantity, current_price)

        else:
            navigation_in_the_buy.click_to_confirm_buy()

        time.sleep(1.5)

        write_to_db.register_sale_of_goods(shared_variables.character_id, name, quantity)

    def selling_by_occult_means(self, name, quantity, current_price):
        required_amount = float(check.check_balance_in_order(default_area_of_screenshot=(732, 845, 840, 880)))
        print(required_amount)
        navigation_in_the_buy.move_and_click(1639, 71)

        inventory = parse_inventory.converting_images_to_strings()
        y_cords_of_goods = 362 + 77 * [index for index, item in enumerate(inventory) if item[0] == name][0]

        navigation_in_the_buy.move_and_click(500, y_cords_of_goods)
        time.sleep(1.5)

        navigation_in_the_buy.move_and_click(1692, 622)

        scan = self.scan_price_and_amount()
        price = scan[0]
        amount = scan[1]

        if price * amount >= required_amount:
            self.sale_of_product_itself(y_cords_of_goods, quantity - self.buying_missing_money(required_amount, price), current_price)

    def scan_price_and_amount(self):
        time.sleep(1)
        price_path = path_to_screenshots + "price_for_sale.png"
        amount_path = path_to_screenshots + "amount_for_sale.png"

        parse_inventory.take_screenshot(price_path, (1293, 359, 1363, 383))
        parse_inventory.take_screenshot(amount_path, (1379, 362, 1439, 380))

        parse_inventory.upscale_image(price_path, 1.5)
        parse_inventory.upscale_image(amount_path, 1.5)

        parse_inventory.delete_all_colors_except_one(price_path, [60, 60, 60], [191, 181, 175])
        parse_inventory.delete_all_colors_except_one(amount_path, [65, 65, 65], [196, 186, 171])

        price = parse_inventory.image_to_string(price_path, True)
        amount = parse_inventory.image_to_string(amount_path, True)

        return float(price), int(amount)

    def buying_missing_money(self, required_amount, price):
        navigation_in_the_buy.move_and_click(1023, 639)
        navigation_in_the_buy.click()

        amount = math.ceil(required_amount / price)

        navigation_in_the_buy.type(str(amount))
        navigation_in_the_buy.move_and_click(1160, 856)

        time.sleep(1.5)

        return amount

    def sale_of_product_itself(self, y_cords_of_goods, quantity, current_price):
        navigation_in_the_buy.move_and_click(500, y_cords_of_goods)
        navigation_in_the_buy.move_and_click(980, 457)

        navigation_in_the_buy.move_to_sell_unit_price_and_set_price(current_price)
        navigation_in_the_buy.move_to_sell_quantity_and_set_quantity(quantity)

        navigation_in_the_buy.click_to_confirm_buy()


