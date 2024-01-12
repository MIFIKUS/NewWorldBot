from NavigationInTheGame.navigation_in_the_game import navigation_in_the_buy


class PurchasingGoodsAtTheBestPrice:
    def search_for_buy_button(self, num_of_list):
        navigation_in_the_buy.go_to_buy_resources()
        navigation_in_the_buy.go_to_buy_refined_resources()

    def buy(self, num_of_list):
        pass


purchasing = PurchasingGoodsAtTheBestPrice()





#1. Проверяет все цены на продажу и там и там
#2. Выявляет актуальные цены в каждой категории
#3. расчитывает разницу покупки и продажи, минимум 20%
#4. По приоритету от большего процента к меньшему и записывать все это в таблицу
#5. Оставляет заявку на покупку по всем балдежным ценам пока бабки не закончатся от большего к меньшему
# ( было бы найс чтоб можно было менять этот процент , в идеале для каждой категории , если слишком сложно , то хотя бы просто чтоб общий процент можно было менять )