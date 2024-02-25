from TraderBot import shared_variables
from TraderBot.DataBase.write_to_db import write_to_db
from TraderBot.NavigationInTheGame.navigation_in_the_buy_tab import navigation_in_the_buy
from TraderBot.ActionsAndChecksInGame.check import check
import time


class PurchasingGoodsAtTheBestPrice:
    def __init__(self, percent, max_price):
        self.max_price = max_price
        self.percent = percent

    def search_for_buy_button(self, list_of_prices_and_amounts):
        navigation_in_the_buy.go_to_buy_resources()
        for el in range(len(list_of_prices_and_amounts)):
            navigation_in_the_buy.go_to_category(list_of_prices_and_amounts[el][0])
            navigation_in_the_buy.click_to_place_buy_order()

            time.sleep(2.7)
            balance = float(check.check_balance_in_order()) + list_of_prices_and_amounts[el][1]

            if balance >= self.max_price + 15:
                self.buy(list_of_prices_and_amounts[el][1], list_of_prices_and_amounts[el][3])
                self._orders_record(list_of_prices_and_amounts[el][0], list_of_prices_and_amounts[el][3])

            elif list_of_prices_and_amounts[el][1] <= balance <= self.max_price + 10:
                self.buy(list_of_prices_and_amounts[el][1],
                         round(abs(balance / (list_of_prices_and_amounts[el][1]) -
                                   balance / (list_of_prices_and_amounts[el][1]) / 100 * 3 - 1)))

                self._orders_record(list_of_prices_and_amounts[el][0],
                                    round(abs(balance / (list_of_prices_and_amounts[el][1]) -
                                              balance / (list_of_prices_and_amounts[el][1]) / 100 * 3 - 1)))

                break

            elif balance < 1:
                navigation_in_the_buy.esc()
                break

            elif list_of_prices_and_amounts[el][1] > balance:
                navigation_in_the_buy.esc()
                break

            navigation_in_the_buy.click_to_buy_resources()

    def _orders_record(self, product_name, quantity):
        write_to_db.record_transactions_goods(shared_variables.character_id, [[product_name, quantity]])

    def buy(self, cost_of_goods, quantity):
        navigation_in_the_buy.move_to_buy_unit_price_and_set_price(cost_of_goods + 0.01)
        navigation_in_the_buy.move_to_buy_quantity_and_set_quantity(quantity)

        navigation_in_the_buy.click_to_confirm_buy()
        time.sleep(1)
