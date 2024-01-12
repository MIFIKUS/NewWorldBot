from parse_buy_order import parse_buy_order
from purchasing_goods_at_the_best_price import purchasing
from parse_sell_order import parse_sell_order


parse_buy_order.start()
parse_sell_order.start()
purchasing.search_for_buy_button(0)
purchasing.search_for_buy_button(3)











#1. Проверяет все цены на продажу ( первая вкладка аукциона )
#2. Выявляет актуальные цены по каждому товару
#3. Идёт в бай ордера и выявляет актуальные цены там
#4. Может выставлять сразу же бай ордер если на этот же товар в продажах разница составляет 20%
# ( было бы найс чтоб можно было менять этот процент , в идеале для каждой категории , если слишком сложно , то хотя бы просто чтоб общий процент можно было менять )