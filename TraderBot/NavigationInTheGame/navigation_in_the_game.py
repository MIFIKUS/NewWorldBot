from MainClasses.MouseAndKeyboard.mouse_actions import Mouse


class Navigation(Mouse):

    def go_to_sell_resources(self):
        self.move_and_click(535, 155)
        self.move_and_click(745, 225)
        self.move_and_click(150, 680)

    def sell_back(self):
        self.move_and_click(260, 395)

    def go_to_buy_resources(self):
        self.move_and_click(250, 145)
        self.move_and_click(130, 600)

    def buy_back(self):
        self.move_and_click(250, 320)

    def go_to_buy_refined_resources(self):
        self.move_and_click(235, 635)


