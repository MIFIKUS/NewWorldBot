from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
from MainClasses.MouseAndKeyboard.keyboard_actions import Keyboard
from TraderBot.Jsons.get_json_data import GetJsonData

categories = GetJsonData.get_json()


class NavigationInSellAllItems(Mouse, Keyboard):

    def go_to_sell_resources(self):
        self.move_and_click(535, 155)
        self.move_and_click(745, 225)
        self.move_and_click(150, 680)

    def sell_back(self):
        self.move_and_click(260, 395)


navigation_in_sell_all_items = NavigationInSellAllItems()

