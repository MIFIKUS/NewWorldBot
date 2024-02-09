from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
from MainClasses.MouseAndKeyboard.keyboard_actions import Keyboard
from TraderBot.ActionsAndChecksInGame.actions import actions
from TraderBot.DataBase.read_db import read_db
import time


class NavigationInCharactersMenu(Mouse, Keyboard):
    def __init__(self):
        super().__init__()
        self.character_id = None

    def _click_to_play(self):
        self.move_and_click(1650, 950)

    def _remove_pop_up_window(self):
        self.move_and_click(1660, 260)

    def _click_to_server_menu(self):
        self.move_and_click(200, 340)

    def _go_back_to_menu(self):
        self.esc()
        time.sleep(1)
        self.esc()
        self.move_and_click(1860, 40)
        self.move_and_click(1270, 715)
        self.move_and_click(1100, 650)
        time.sleep(30)
        self._remove_pop_up_window()
        self._click_to_play()

    def character_buster(self, function):
        cords = read_db.switching_between_characters()

        for i in cords:
            self._click_to_server_menu()
            time.sleep(30)

            self._remove_pop_up_window()

            self.character_id = i[0]

            self.move_and_click(i[1], i[2])
            time.sleep(20)
            self.move_and_click(i[3], i[4])

            self._click_to_play()
            time.sleep(90)

            actions.open_an_auction()
            function()
            self._go_back_to_menu()


navigation_in_characters_menu = NavigationInCharactersMenu()

