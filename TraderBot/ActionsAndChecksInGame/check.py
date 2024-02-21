from MainClasses.Image.image import Image
from TraderBot.shared_variables import path_to_screenshots
import time


class Check(Image):
    '''Класс в котоором проверяются различные значения внутри игры'''
    def check_balance(self):
        '''Проверить баланс'''
        time.sleep(1)
        path_to_balance_picture = path_to_screenshots + "balance.png"
        self.take_screenshot(path_to_balance_picture, (1700, 20, 1820, 50))
        self.delete_all_colors_except_one(path_to_balance_picture, [190, 180, 165], [255, 255, 255])
        balance = self.image_to_string(path_to_balance_picture, True)

        balance = balance.replace(',', '').replace('\n', '')
        if len(balance) >= 7:
            if balance[1] == '.':
                balance = balance.replace('.', '', 1)
            if balance[2] == '.':
                balance = balance.replace('.', '', 1)
            if balance[3] == '.':
                balance = balance.replace('.', '', 1)

        return balance

    def check_balance_in_order(self, default_area_of_screenshot=(975, 820, 1240, 860)):
        time.sleep(1)
        path_to_balance_picture = path_to_screenshots + "balance.png"
        self.take_screenshot(path_to_balance_picture, default_area_of_screenshot)
        self.delete_all_colors_except_one(path_to_balance_picture, [125, 125, 125], [255, 255, 255])
        balance = self.image_to_string(path_to_balance_picture, True)

        balance = balance.replace(',', '').replace('\n', '')
        if len(balance) >= 7:
            if balance[1] == '.':
                balance = balance.replace('.', '', 1)
            if balance[2] == '.':
                balance = balance.replace('.', '', 1)
            if balance[3] == '.':
                balance = balance.replace('.', '', 1)

        return balance

    def check_for_red(self):
        img_path = path_to_screenshots + 'check_for_red.png'
        self.take_screenshot(img_path, (1121, 995, 1162, 1002))
        color = self.get_main_color(img_path)
        return color


check = Check()



