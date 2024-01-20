from TraderBot.Parsing.parse_buy_order import parse_buy_order
from TraderBot.Parsing.parse_sell_order import parse_sell_order
from TraderBot.Calculation.price_calculation import PriceCalculation
from TraderBot.Trading.purchasing_goods_at_the_best_price import PurchasingGoodsAtTheBestPrice
from ActionsAndChecksInGame.actions import actions

max_price = 1000
percent = 20

parse_buy_order.start()
actions.bypass_afk()
parse_sell_order.start()
actions.bypass_afk()

price_calculation = PriceCalculation(max_price)
price_calculation.record_price_difference_in_table()

purchasing = PurchasingGoodsAtTheBestPrice(percent, max_price)
purchasing.search_for_buy_button(price_calculation.calculating_price_difference())



#def start():
#    windows.switch_windows(a)
#def a(hwnd):
#start()











#1. Проверяет все цены на продажу и там и там
#2. Выявляет актуальные цены в каждой категории
#3. расчитывает разницу покупки и продажи, минимум 20%
#4. По приоритету от большего процента к меньшему и записывать все это в таблицу
#5. Оставляет заявку на покупку по всем балдежным ценам пока бабки не закончатся от большего к меньшему
# ( было бы найс чтоб можно было менять этот процент , в идеале для каждой категории , если слишком сложно , то хотя бы просто чтоб общий процент можно было менять )