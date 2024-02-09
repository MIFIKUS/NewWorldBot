from MainClasses.MouseAndKeyboard.keyboard_actions import Keyboard
from MainClasses.MouseAndKeyboard.mouse_actions import Mouse


class Actions(Mouse, Keyboard):
    def bypass_afk(self):
        self.esc()
        self.press_button('w')
        self.press_button('s')
        self.press_button('e')

    def open_an_auction(self):
        self.hold_down_button('s', 2)
        self.hold_down_button('w', 2)
        self.press_button('e')


actions = Actions()
