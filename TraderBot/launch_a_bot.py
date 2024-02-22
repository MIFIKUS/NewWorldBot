import time

from Calculation.price_calculation import PriceCalculation
from TraderBot.DataBase.write_to_db import write_to_db
from Trading.purchasing_goods_at_the_best_price import PurchasingGoodsAtTheBestPrice
from Trading.sale_goods_at_the_best_price import SaleGoodsAtTheBestPrice
from ActionsAndChecksInGame.actions import actions
from NavigationInTheGame.navigation_in_the_characters_menu import navigation_in_characters_menu
from ActionsAndChecksInGame.check import check
from MainClasses.Windows.windows import Windows
import TraderBot.shared_variables as shared_variables

windows = Windows()

max_price = shared_variables.max_price
percent = shared_variables.percent
poverty_threshold = shared_variables.poverty_threshold


class StartupCluster:
    def __init__(self, poverty_threshold_startup):
        self.poverty_threshold = poverty_threshold_startup

    def part_of_purchase(self, hwnd):
        self.moving_between_characters(self.script_for_purchase)

    def part_of_sale(self):
        self.moving_between_characters(self.script_for_sale)

    def script_for_purchase(self):
        self.setting_character_parameters()
        self.parsing()
        self.buy()

    def script_for_sale(self):
        self.sale()

    def moving_between_characters(self, func):
        navigation_in_characters_menu.character_buster(func)

    def setting_character_parameters(self):
        balance = float(check.check_balance())

        if balance < self.poverty_threshold:
            shared_variables.checking_for_beggar = True
            shared_variables.balance_of_beggar = balance
        else:
            shared_variables.checking_for_beggar = False

    def parsing(self):
        from Parsing.parse_buy_order import parse_buy_order
        from Parsing.parse_sell_order import parse_sell_order
        try:
            parse_buy_order.get_categories()
            actions.bypass_afk()
            parse_sell_order.get_categories()
            actions.bypass_afk()
        except ValueError:
            write_to_db.delete_all_orders()
            parse_buy_order.get_categories()
            actions.bypass_afk()
            parse_sell_order.get_categories()
            actions.bypass_afk()

    def buy(self):
        price_calculation = PriceCalculation(max_price, percent)
        purchasing = PurchasingGoodsAtTheBestPrice(percent, max_price)
        price_calculation.record_price_difference_in_table()
        purchasing.search_for_buy_button(price_calculation.calculating_price_difference())

    def sale(self):
        sale_goods_at_the_best_price = SaleGoodsAtTheBestPrice()
        sale_goods_at_the_best_price.quantity_comparison()


startup_cluster = StartupCluster(poverty_threshold)

#write_to_db.delete_all_orders()
#write_to_db.delete_character_positions(3, 'purchase_and_sale')

write_to_db.delete_all_orders()
windows.switch_windows(startup_cluster.part_of_purchase)
for _ in range(3):
    startup_cluster.part_of_sale()
    time.sleep(360)

