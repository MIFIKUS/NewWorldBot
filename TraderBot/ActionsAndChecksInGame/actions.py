from MainClasses.MouseAndKeyboard.keyboard_actions import Keyboard
from MainClasses.MouseAndKeyboard.mouse_actions import Mouse


class Actions(Mouse, Keyboard):
    def bypass_afk(self):
        self.esc()
        self.press_button('w')
        self.press_button('s')
        self.press_button('e')


actions = Actions()