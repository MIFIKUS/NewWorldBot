from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
from MainClasses.MouseAndKeyboard.keyboard_actions import Keyboard
from TraderBot.Jsons.get_json_data import GetJsonData

categories = GetJsonData.get_json()


class NavigationInSellMyItems(Mouse, Keyboard):
    def go_to_my_items(self):
        self.move_and_click(535, 155)
        self.move_and_click(325, 230)
        self.move_and_click(600, 295)
        self.move_and_click(600, 295)


navigation_in_the_sell_my_items = NavigationInSellMyItems()





#668,311
#677, 1038