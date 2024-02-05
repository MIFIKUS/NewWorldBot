from MainClasses.MouseAndKeyboard.mouse_actions import Mouse
import json

with (open("E:\\projects\\NewWorldBot\\TraderBot\\Jsons\\coordinates_in_the_characters_menu.json", 'r', encoding='utf-8')
      as data):
    characters = json.load(data)


class NavigationInCharactersMenu(Mouse):
    def click_to_play(self):
        self.move_and_click(1650, 950)

    def remove_pop_up_window(self):
        self.move_and_click(1805, 130)

    def click_to_server_menu(self):
        self.move_and_click(200, 340)
    
    @staticmethod
    def character_buster():
        coordinates_of_servers = [i for i in characters.keys()]
        for i in coordinates_of_servers:
            print(characters[i]["cords"], characters[i]["characters"])
        return coordinates_of_servers
