from TraderBot.NavigationInTheGame.navigation_in_the_buy_tab import navigation_in_the_buy
from TraderBot.ActionsAndChecksInGame.check import check
from TraderBot.Jsons.get_json_data import GetJsonData
import time


class PurchasingGoodsAtTheBestPrice:
    def __init__(self, percent, max_price):
        self.max_price = max_price
        self.percent = percent

    def search_for_buy_button(self, list_of_prices_and_amounts):

        navigation_in_the_buy.go_to_buy_resources()
        for el in range(len(list_of_prices_and_amounts)):

            navigation_in_the_buy.go_to_buy_catalog_of_resources(list_of_prices_and_amounts[el][0])
            navigation_in_the_buy.go_to_category(list_of_prices_and_amounts[el][0])
            navigation_in_the_buy.click_to_place_buy_order()
            if float(check.check_balance()) >= self.max_price + 10:
                self.buy(list_of_prices_and_amounts[el][1], list_of_prices_and_amounts[el][3])
            elif list_of_prices_and_amounts[el][1] <= float(check.check_balance()) <= self.max_price + 10:
                self.buy(list_of_prices_and_amounts[el][1],
                         list_of_prices_and_amounts[el][3] / GetJsonData.balance_of_beggar)
            navigation_in_the_buy.click_to_buy_resources()

    def buy(self, cost_of_goods, quantity):
        navigation_in_the_buy.move_to_buy_unit_price_and_set_price(cost_of_goods + 0.01)
        navigation_in_the_buy.move_to_buy_quantity_and_set_quantity(quantity)

        navigation_in_the_buy.click_to_confirm_buy()
        time.sleep(1)








#1. Проверяет все цены на продажу и там и там
#2. Выявляет актуальные цены в каждой категории
#3. расчитывает разницу покупки и продажи, минимум 20%
#4. По приоритету от большего процента к меньшему и записывать все это в таблицу
#5. Оставляет заявку на покупку по всем балдежным ценам пока бабки не закончатся от большего к меньшему
# ( было бы найс чтоб можно было менять этот процент , в идеале для каждой категории , если слишком сложно , то хотя бы просто чтоб общий процент можно было менять )