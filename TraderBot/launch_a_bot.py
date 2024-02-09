from Parsing.parse_buy_order import parse_buy_order
from Parsing.parse_sell_order import parse_sell_order
from Calculation.price_calculation import PriceCalculation
from Trading.purchasing_goods_at_the_best_price import PurchasingGoodsAtTheBestPrice
from Trading.sale_goods_at_the_best_price import sale_goods_at_the_best_price
from ActionsAndChecksInGame.actions import actions
from NavigationInTheGame.navigation_in_the_characters_menu import navigation_in_characters_menu
from ActionsAndChecksInGame.check import check
from Jsons.get_json_data import GetJsonData
from MainClasses.Windows.windows import Windows

windows = Windows()

max_price = 1000
percent = 20


class StartupCluster:
    def part_of_purchase(self):
        self.moving_between_characters(self.script_for_purchase())

    def part_of_sale(self):
        self.moving_between_characters(self.script_for_sale())

    def script_for_purchase(self):
        self.setting_character_parameters()
        self.parsing()
        self.buy()

    def script_for_sale(self):
        self.sale()

    def moving_between_characters(self, func):
        navigation_in_characters_menu.character_buster(func)

    def setting_character_parameters(self):
        if float(check.check_balance()) < 3000:
            GetJsonData.checking_for_beggar = True
            GetJsonData.balance_of_beggar = float(check.check_balance())
        else:
            GetJsonData.checking_for_beggar = False

    def parsing(self):
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
        sale_goods_at_the_best_price.quantity_comparison()


startup_cluster = StartupCluster()

windows.switch_windows(startup_cluster.part_of_purchase())
startup_cluster.part_of_sale()

#mouse = Mouse()
#windows = Windows()
#
#
#def start():
#    windows.switch_windows(ac)
#
#
#def ac(hwnd):
#    mouse.move(676, 311 + 51)
#    mouse.drag(676, 311 + 51 + int(51 / 9.52 * 10) + int(51 / 9.52 * 11))
#
#
#start()






#1. Проверяет все цены на продажу и там и там
#2. Выявляет актуальные цены в каждой категории
#3. расчитывает разницу покупки и продажи, минимум 20%
#4. По приоритету от большего процента к меньшему и записывать все это в таблицу
#5. Оставляет заявку на покупку по всем балдежным ценам пока бабки не закончатся от большего к меньшему
# ( было бы найс чтоб можно было менять этот процент , в идеале для каждой категории , если слишком сложно , то хотя бы просто чтоб общий процент можно было менять )